from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
from toontown.coghq import BossbotHQExterior
from toontown.coghq import BossbotHQBossBattle
from toontown.coghq import BossbotOfficeExterior
from toontown.coghq import CountryClubInterior
from toontown.battle import BattleParticles
from pandac.PandaModules import DecalEffect, TextEncoder
import random
aspectSF = 0.7227

class BossbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('BossbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('countryClubInterior', self.enterCountryClubInterior, self.exitCountryClubInterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('countryClubInterior')

        self.musicFile = random.choice(['phase_12/audio/bgm/Bossbot_Entry_v1.ogg', 'phase_12/audio/bgm/Bossbot_Entry_v2.ogg', 'phase_12/audio/bgm/Bossbot_Entry_v3.ogg'])
        self.cogHQExteriorModelPath = 'phase_12/models/bossbotHQ/CogGolfHub'
        self.cogHQLobbyModelPath = 'phase_12/models/bossbotHQ/CogGolfCourtyard'
        self.geom = None
        self.rain = None
        self.rainRender = None
        self.rainSound = None
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
       # self.startRain()
        Toon.loadBossbotHQAnims()
        
    def startRain(self):
        #if not config.GetBool('want-particle-effects', True):
           # return
        #if self.geom is None:
            #return
        self.rain = BattleParticles.loadParticleFile('raindisk.ptf')
        self.rain.setPos(0, 0, 20)
        self.rainRender = render.attachNewNode('rainRender')
        self.rainRender.setDepthWrite(0)
        self.rainRender.setBin('fixed', 1)
        self.rain.start(camera, self.rainRender)
        self.rainSound = base.loadSfx('phase_12/audio/sfx/CHQ_rain_ambient.ogg')
        base.playSfx(self.rainSound, looping=1, volume=0.1)

    def stopRain(self):
        if self.rain:
            self.rain.cleanup()
            self.rainSound.stop()
            
    def unloadPlaceGeom(self):
        del self.rain
        del self.rainRender
        del self.rainSound
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        self.notify.debug('zoneId = %d ToontownGlobals.BossbotHQ=%d' % (zoneId, ToontownGlobals.BossbotHQ))
        if zoneId == ToontownGlobals.BossbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            gzLinkTunnel = self.geom.find('**/LinkTunnel1')
            gzLinkTunnel.setName('linktunnel_gz_17000_DNARoot')
            self.makeSigns()
            top = self.geom.find('**/TunnelEntrance')
            origin = top.find('**/tunnel_origin')
            origin.setH(-33.33)
        elif zoneId == ToontownGlobals.BossbotLobby:
            if config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit BossbotLobby')
            self.notify.debug('cogHQLobbyModelPath = %s' % self.cogHQLobbyModelPath)
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def makeSigns(self):

        def makeSign(topStr, signStr, textId):
            top = self.geom.find('**/' + topStr)
            sign = top.find('**/' + signStr)
            locator = top.find('**/sign_origin')
            signText = DirectGui.OnscreenText(text=TextEncoder.upper(TTLocalizer.GlobalStreetNames[textId][-1]), font=ToontownGlobals.getSuitFont(), scale=TTLocalizer.BCHQLsignText, fg=(0, 0, 0, 1), parent=sign)
            signText.setPosHpr(locator, 0, -0.1, -0.25, 0, 0, 0)
            signText.setDepthWrite(0)

        makeSign('Gate_2', 'Sign_6', 10700)
        makeSign('TunnelEntrance', 'Sign_2', 1000)
        makeSign('Gate_3', 'Sign_3', 10600)
        makeSign('Gate_4', 'Sign_4', 10500)
        makeSign('GateHouse', 'Sign_5', 10200)

    def enterStageInterior(self, requestStatus):
        self.placeClass = StageInterior.StageInterior
        self.stageId = requestStatus['stageId']
        self.enterPlace(requestStatus)
        #self.startRain()

    def exitStageInterior(self):
       # self.stopRain()
        self.exitPlace()
        self.placeClass = None
        return

    def getExteriorPlaceClass(self):
        self.notify.debug('getExteriorPlaceClass')
        return BossbotHQExterior.BossbotHQExterior

    def getBossPlaceClass(self):
        self.notify.debug('getBossPlaceClass')
        return BossbotHQBossBattle.BossbotHQBossBattle

    def enterFactoryExterior(self, requestStatus):
        #self.startRain()
        self.placeClass = BossbotOfficeExterior.BossbotOfficeExterior
        self.enterPlace(requestStatus)

    def exitFactoryExterior(self):
        #self.stopRain()
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None
        return

    def enterCogHQBossBattle(self, requestStatus):
        self.notify.debug('BossbotCogHQLoader.enterCogHQBossBattle')
        CogHQLoader.CogHQLoader.enterCogHQBossBattle(self, requestStatus)
        base.cr.forbidCheesyEffects(1)

    def exitCogHQBossBattle(self):
        self.notify.debug('BossbotCogHQLoader.exitCogHQBossBattle')
        CogHQLoader.CogHQLoader.exitCogHQBossBattle(self)
        base.cr.forbidCheesyEffects(0)

    def enterCountryClubInterior(self, requestStatus):
        self.placeClass = CountryClubInterior.CountryClubInterior
        self.notify.info('enterCountryClubInterior, requestStatus=%s' % requestStatus)
        self.countryClubId = requestStatus['countryClubId']
        self.enterPlace(requestStatus)

    def exitCountryClubInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.countryClubId
        return
