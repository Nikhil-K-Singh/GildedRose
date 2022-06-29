# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items,q_min=0,q_max=50,q_legendary=80):
        self.items = items
        self.q_min = q_min
        self.q_max = q_max
        self.q_legendary = q_legendary

    def update_standard(self,item):
        if item.quality > self.q_min:   #   The Quality of an item is never negative
            item.quality -= 1
            if item.sell_in <= 0:   #   Once the sell by date has passed, Quality degrades twice as fast
                item.quality -= 1
        item.sell_in -= 1   # sell_in time decreases regardless
        
    def update_aged_brie(self,item):
        if item.quality < self.q_max:   # "Aged Brie" actually increases in Quality the older it gets
            item.quality+=1
            if item.sell_in <=0:
                item.quality += 1
        item.sell_in -= 1   # sell_in time decreases regardless
        if item.quality > self.q_max:   #   The Quality of an item is never more than 50
            item.quality = self.q_max
        

    def update_backstage(self,item):
        if 10 >= item.sell_in > 5:  #   Quality increases by 2 when there are 10 days or less      
            item.quality +=2
        elif 5 >= item.sell_in > 0: #   and by 3 when there are 5 days or less
            item.quality +=3
        elif item.sell_in <= 0: #   Quality drops to 0 after the concert
            item.quality = 0
        else:
            item.quality +=1

        if item.quality > self.q_max:   #   The Quality of an item is never more than 50
            item.quality = self.q_max

        item.sell_in -= 1   # sell_in decreases regardless
    
    def update_conjured(self,item):
        if item.quality > self.q_min:   #   "Conjured" items degrade in Quality twice as fast as normal items
            item.quality-=2 
            if item.sell_in <=0:    #   Once the sell by date has passed, Quality degrades twice as fast
                item.quality-=2 
        if item.quality < self.q_min:   #   The Quality of an item is never negative
            item.quality = self.q_min

        item.sell_in -= 1   # sell_in decreases regardless

    def update_quality(self):   
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue    # since sulfuras does not decrease in quality and there's no limitation for sell_in 
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