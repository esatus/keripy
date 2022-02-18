# -*- encoding: utf-8 -*-
"""
tests.app.agenting module

"""

from hio.base import doing

from keri import kering
from keri.core import coring
from keri.help import nowIso8601
from keri.app import habbing, indirecting, agenting
from keri.core.eventing import SealSource
from keri.db import dbing
from keri.vdr import eventing, viring, issuing


def test_withness_receiptor(seeder):
    with habbing.openHby(name="wan", salt=coring.Salter(raw=b'wann-the-witness').qb64) as wanHby, \
            habbing.openHby(name="wil", salt=coring.Salter(raw=b'will-the-witness').qb64) as wilHby, \
            habbing.openHby(name="wes", salt=coring.Salter(raw=b'wess-the-witness').qb64) as wesHby, \
            habbing.openHby(name="pal", salt=coring.Salter(raw=b'0123456789abcdef').qb64) as palHby:

        seeder.seedWitEnds(palHby.db, protocols=[kering.Schemes.tcp])
        wanDoers = indirecting.setupWitness(alias="wan", hby=wanHby, tcpPort=5632, httpPort=5642)
        wilDoers = indirecting.setupWitness(alias="wil", hby=wilHby, tcpPort=5633, httpPort=5643)
        wesDoers = indirecting.setupWitness(alias="wes", hby=wesHby, tcpPort=5634, httpPort=5644)

        wanHab = wanHby.habByName(name="wan")
        wilHab = wilHby.habByName(name="wil")
        wesHab = wesHby.habByName(name="wes")

        palHab = palHby.makeHab(name="pal", wits=[wanHab.pre, wilHab.pre, wesHab.pre], transferable=True)

        witDoer = agenting.WitnessReceiptor(hby=palHby)
        witDoer.msgs.append(dict(pre=palHab.pre))

        limit = 5.0
        tock = 0.03125
        doist = doing.Doist(limit=limit, tock=tock)
        doers = wanDoers + wilDoers + wesDoers + [witDoer]
        doist.do(doers=doers)

        kev = palHab.kever
        ser = kev.serder
        dgkey = dbing.dgKey(ser.preb, ser.saidb)

        wigs = wanHab.db.getWigs(dgkey)
        assert len(wigs) == 3
        wigs = wilHab.db.getWigs(dgkey)
        assert len(wigs) == 3
        wigs = wesHab.db.getWigs(dgkey)
        assert len(wigs) == 3


def test_witness_sender(seeder):
    with habbing.openHby(name="wan", salt=coring.Salter(raw=b'wann-the-witness').qb64) as wanHby, \
            habbing.openHby(name="wil", salt=coring.Salter(raw=b'will-the-witness').qb64) as wilHby, \
            habbing.openHby(name="wes", salt=coring.Salter(raw=b'wess-the-witness').qb64) as wesHby, \
            habbing.openHby(name="pal", salt=coring.Salter(raw=b'0123456789abcdef').qb64) as palHby:

        wanDoers = indirecting.setupWitness(alias="wan", hby=wanHby, tcpPort=5632, httpPort=5642)
        wilDoers = indirecting.setupWitness(alias="wil", hby=wilHby, tcpPort=5633, httpPort=5643)
        wesDoers = indirecting.setupWitness(alias="wes", hby=wesHby, tcpPort=5634, httpPort=5644)
        seeder.seedWitEnds(palHby.db, protocols=[kering.Schemes.tcp])

        wanHab = wanHby.habByName(name="wan")
        wilHab = wilHby.habByName(name="wil")
        wesHab = wesHby.habByName(name="wes")

        palHab = palHby.makeHab(name="pal", wits=[wanHab.pre, wilHab.pre, wesHab.pre], transferable=True)

        serder = eventing.issue(vcdig="Ekb-iNmnXnOYIAlZ9vzK6RV9slYiKQSyQvAO-k0HMOI8",
                                regk="EbA1o_bItVC9i6YB3hr2C3I_Gtqvz02vCmavJNoBA3Jg")
        seal = SealSource(s=palHab.kever.sn, d=palHab.kever.serder.said)
        msg = issuing.Issuer.attachSeal(serder=serder, seal=seal)

        witDoer = agenting.WitnessPublisher(hab=palHab, msg=msg)

        limit = 1.0
        tock = 0.03125
        doist = doing.Doist(limit=limit, tock=tock)
        doers = wanDoers + wilDoers + wesDoers + [witDoer]
        doist.do(doers=doers)

        assert witDoer.done is True

        for name in ["wes", "wil", "wan"]:
            reger = viring.Registry(name=name)
            raw = reger.getTvt(dbing.dgKey(serder.preb, serder.saidb))
            found = coring.Serder(raw=bytes(raw))
            assert serder.pre == found.pre


def test_witness_inquisitor(mockHelpingNowUTC, seeder):
    with habbing.openHby(name="wan", salt=coring.Salter(raw=b'wann-the-witness').qb64) as wanHby, \
            habbing.openHby(name="wil", salt=coring.Salter(raw=b'will-the-witness').qb64) as wilHby, \
            habbing.openHby(name="wes", salt=coring.Salter(raw=b'wess-the-witness').qb64) as wesHby, \
            habbing.openHby(name="pal", salt=coring.Salter(raw=b'0123456789abcdef').qb64) as palHby, \
            habbing.openHby(name="qin", salt=coring.Salter(raw=b'abcdef0123456789').qb64) as qinHby:
        wanDoers = indirecting.setupWitness(alias="wan", hby=wanHby, tcpPort=5632, httpPort=5642)
        wilDoers = indirecting.setupWitness(alias="wil", hby=wilHby, tcpPort=5633, httpPort=5643)
        wesDoers = indirecting.setupWitness(alias="wes", hby=wesHby, tcpPort=5634, httpPort=5644)
        seeder.seedWitEnds(palHby.db, protocols=[kering.Schemes.tcp])
        seeder.seedWitEnds(qinHby.db, protocols=[kering.Schemes.tcp])

        wanHab = wanHby.habByName(name="wan")
        wilHab = wilHby.habByName(name="wil")
        wesHab = wesHby.habByName(name="wes")

        palHab = palHby.makeHab(name="pal", wits=[wanHab.pre, wilHab.pre, wesHab.pre], transferable=True)
        qinHab = qinHby.makeHab(name="qin", wits=[wanHab.pre, wilHab.pre, wesHab.pre], transferable=True)

        palWitDoer = agenting.WitnessReceiptor(hby=palHby)
        palWitDoer.msgs.append(dict(pre=palHab.pre))
        qinWitDoer = agenting.WitnessReceiptor(hby=qinHby)
        qinWitDoer.msgs.append(dict(pre=qinHab.pre))
        qinWitq = agenting.WitnessInquisitor(hab=qinHab)

        # query up a few to make sure it still works
        stamp = nowIso8601()  # need same time stamp or not duplicate
        qinWitq.query(pre=palHab.pre, stamp=stamp)
        qinWitq.query(pre=palHab.pre, stamp=stamp)
        qinWitq.query(pre=palHab.pre, stamp=stamp)
        palWitq = agenting.WitnessInquisitor(hab=palHab)
        palWitq.query(pre=qinHab.pre, stamp=stamp)

        limit = 1.0
        tock = 0.03125
        doist = doing.Doist(limit=limit, tock=tock)
        doers = wanDoers + wilDoers + wesDoers + [palWitDoer, qinWitDoer]
        doist.do(doers=doers)

        for hab in [palHab, qinHab]:
            kev = hab.kever
            ser = kev.serder
            dgkey = dbing.dgKey(ser.preb, ser.saidb)

            wigs = wanHab.db.getWigs(dgkey)
            assert len(wigs) == 3
            wigs = wilHab.db.getWigs(dgkey)
            assert len(wigs) == 3
            wigs = wesHab.db.getWigs(dgkey)
            assert len(wigs) == 3

        doist = doing.Doist(limit=limit, tock=tock)
        doers = wanDoers + wilDoers + wesDoers + [qinWitq, palWitq]
        doist.do(doers=doers)

        assert palHab.pre in qinHab.kevers
        assert qinHab.pre in palHab.kevers
