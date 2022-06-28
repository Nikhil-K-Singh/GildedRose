# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items,q_min=0,q_max=50,q_legendary=80):
        self.items = items
        self.q_min = q_min
        self.q_max = q_max
        self.q_legendary = q_legendary

    def update_standard(self,item):
        if item.quality > self.q_min:
            item.quality -= 1
            if item.sell_in <= 0:
                item.quality -= 1
        item.sell_in -= 1
        
    def update_aged_brie(self):
        pass
    def update_sulfuras(self):
        pass

    def update_backstage(self,item):
        if 10 >= item.sell_in > 5:
            item.quality +=2
        elif 5 >= item.sell_in > 0:
            item.quality +=3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality +=1

        if item.quality > self.q_max:
            item.quality = self.q_max

        item.sell_in -= 1
    
    def update_conjured(self,item):
        if item.quality > self.q_min:
            item.quality-=2
            if item.sell_in <=0:
                item.quality-=2
        if item.quality < self.q_min:
            item.quality = self.q_min

        item.sell_in -= 1
        
    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage(item)
            elif item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            else:
                self.update_standard(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)