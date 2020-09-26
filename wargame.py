import random


country = ['US','Russia','UK','Pakistan','India','China']
group1 = []
group2 = []


for i in range(3):
    temp = random.choice(country)
    group1.append(temp)
    country.remove(temp)


group2 = country

print(group1)
print(group2)


del country


india = {'tanks':4795,'soldiers':2999500,'fighter_jets':538,'aircraft_carriers':4,'nuclear_bombs':120}
us = {'tanks':8370,'soldiers':2205050,'fighter_jets':2085,'aircraft_carriers':80,'nuclear_bombs':6970}
russia = {'tanks':13020,'soldiers':2900000,'fighter_jets':873,'aircraft_carriers':20,'nuclear_bombs':7300}
uk = {'tanks':227,'soldiers':228350,'fighter_jets':133,'aircraft_carriers':56,'nuclear_bombs':215}
china = {'tanks':6360,'soldiers':2545000,'fighter_jets':1232,'aircraft_carriers':3,'nuclear_bombs':260}
pakistan = {'tanks':1220,'soldiers':1167500,'fighter_jets':356,'aircraft_carriers':0,'nuclear_bombs':110}

print(india)
print(us)
print(russia)
print(uk)
print(china)
print(pakistan)



class Warfare:
    def __init__(self, tanks, soldiers, fighter_jets, aircraft_carriers, nuclear_bombs):
        self.tanks = tanks
        self.soldiers = soldiers
        self.figher_jets = fighter_jets
        self.aircraft_carriers = aircraft_carriers
        self.nuclear_bombs = nuclear_bombs

    def random_increase(self):
        self.tanks = self.tanks*random.randrange(0.5,1.5)
        self.soldiers = self.soldiers*random.randrange(0.5,1.5)
        self.figher_jets = self.fighter_jets*random.randrange(0.5,1.5)
        self.aircraft_carriers = self.aircraft_carriers*random.randrange(0.5,1.5)
        self.nuclear_bombs = self.nuclear_bombs*random.randrange(0.5,1.5)


    def calculation(self):
        total_random_strength = self.tanks*100 + self.soldiers*1 + self.fighter_jets*1000 + self.aircraft_carriers*10000 + self.nuclear_bombs*10000000 
        return total_random_strength


US, Russia = Warfare(**us), Warfare(**russia)
print(dir(US))
print(dir(Russia))


def comparision():
    while(US.calculation()>(10/100)*US.calculation() or Russia.calculation()>(10/100)*Russia.calculation()):
        a = []
        b = []
        k = US.calculation()
        s = Russia.calculation()
        if k>s:
            k = (25*100)/k
            r = (50*100)/r
            a.append('USA')
        else:
            r=(25*100)/r
            k=(50*100)/k
            b.append('Russia')
        return a,b


print(comparision())