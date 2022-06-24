from gilded_rose import *
import sys
from approvaltests.approvals import verify


def test_gilded_rose():
    content = 'start\n'
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 2
    for day in range(days):
        content = content + "-------- day " + str(day) + "--------\n"
        content = content + "name, sellIn, quality\n"
        for item in items:
            content = content + item.print()
        content = content + "\n"
        GildedRose(items).update_quality()

    content = content + "end\n"
    verify(content)
