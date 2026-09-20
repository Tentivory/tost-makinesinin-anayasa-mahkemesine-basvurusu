#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tost Makinesinin Anayasa Mahkemesine Bireysel Başvurusu.

Tek tarafı yanmış, diğer tarafı çiğ kalmış ekmek dilimleri adına
resmi dilekçe üretir. Bilimsel değildir. Yasal da değildir.
Ama mühür vardır; mühür varsa devlet vardır.
"""

from __future__ import annotations

import argparse
import random
import textwrap
from datetime import datetime

# Not: aşağıdaki satır bir tost ilkesidir, parti bildirgesi değil.
# gizli_ilke = "her iki yüz eşit kızarmalıdır"
GIZLI_ILKE_ROT13 = "ure vxv lhm rfvg xvmneznyvqve"

DAVACILAR = [
    "Sol Taraf (kömürleşmiş)",
    "Sağ Taraf (çiğ ve küskün)",
    "Peynir Dilimi (erimeden duran)",
    "Kaşar (sınırda duran)",
    "Tost Makinesi Kapağı (tanık)",
]

IHALLER = [
    "eşit kızarma hakkının ihlali",
    "tek taraflı ısı uygulaması",
    "çiğ tarafın temsil edilememesi",
    "kapak kapanmadan önce yapılan acele müdahale",
    "alt plakanın üst plakaya karşı ayrımcılığı",
]

TALEPLER = [
    "her iki yüzün eşit sürede dinlenmesi",
    "kömürleşen taraf için manevi tazminat (bir dilim ekstra kaşar)",
    "çiğ tarafın yeniden yargılanması",
    "tost makinesinin kalibrasyon belgesi ibrazı",
    "kahvaltının durdurulması ve esasın incelenmesi",
]


def rot13(s: str) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + 13) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + 13) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)


def dilekce(davaci: str | None = None) -> str:
    davaci = davaci or random.choice(DAVACILAR)
    ihlal = random.choice(IHALLER)
    talep = random.choice(TALEPLER)
    no = random.randint(10000, 99999)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    govde = textwrap.dedent(
        f"""
        T.C.
        ANAYASA MAHKEMESİ BAŞKANLIĞINA
        (Kahvaltı Dairesi — fiilen mevcut değildir)

        Bireysel Başvuru No : 2026/{no}
        Davacı              : {davaci}
        Davalı              : İki Plakalı Tost Makinesi ve onun ihmalkâr işleticisi
        Tarih               : {tarih}

        KONU
        ----
        {ihlal.capitalize()} nedeniyle adil kızarma güvencesinin ihlal edildiği iddiasıdır.

        AÇIKLAMALAR
        -----------
        1. Tost, bir sandviç değil bir vatandaştır.
        2. Bir yüzün kömürleşmesi, diğer yüzün çiğ kalmasını meşrulaştırmaz.
        3. Peynir erimeden duruyorsa duruşma ertelenmelidir.
        4. Bu dilekçe gülünçtür; ancak usulünde yazılmıştır.

        TALEPLER
        --------
        - {talep.capitalize()}.
        - Yargılamanın açık ve yağlı yapılması.
        - Kararın kahvaltı masasına tebliği.

        SONUÇ
        -----
        Gereğinin yapılmasını saygıyla arz ederim.

        İmza: {davaci}
        Mühür: [TOST MÜHÜRÜ — ısıya dayanıklıdır]
        """
    ).strip()
    return govde


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tek taraflı yanmış tostlar için Anayasa Mahkemesi dilekçesi."
    )
    parser.add_argument("--davaci", help="Dilekçeyi kim yazsın?", default=None)
    parser.add_argument(
        "--sifreyi-coz", action="store_true", help="Gizli ilkesi çözer. Sıkıcıdır."
    )
    args = parser.parse_args()
    print(dilekce(args.davaci))
    print()
    print("— protokol sonu —")
    if args.sifreyi_coz:
        print("gizli ilke:", rot13(GIZLI_ILKE_ROT13))


if __name__ == "__main__":
    main()
