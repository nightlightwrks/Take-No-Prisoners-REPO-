init python:
    
    def clamp(num, mini, maxi):
        if num < mini:
            num = mini
        elif num > maxi:
            num = maxi 
    
    class Twod6:
        def __call__(self):
            a = renpy.random.randint(1, 6)
            b = renpy.random.randint(1, 6)
            
            return a, b
    
    def success_rate(mood, dice):
        if sum(dice) - mood <=0:
            print(dice)
            return True
        else:
            print(dice)
            return False 
        
    
    

            
    class Aero:
        def __init__(self, chara, stats, mood):
            self.c = chara
            self.stats = stats
            self.mood = mood 
        
        def statMath(self, stat, value):
            self.stats[stat] += value 
            
            clamp(self.stats[stat], 0, 100)
        
        def moodMath(self, value):
            self.mood += value 
            clamp(self.mood, 1, 12)
        
        @property 
        def g_mood(self):
            return self.mood 
        
        
        
        def stat_num(self, name):
            return self.stats[name]
            
    
    class Jobsystem:
        def __init__(self, name, niceName, desc, statpay):
            self.name = name
            self.niceName = niceName
            self.desc = desc
            self.statpay = statpay 
            
        
        def statGains(self, success):
            if success:
                riot = self.statpay
                riot.popitem()
            for k, v in riot.items():
                aero.statMath(k, v)
            else:
                for k, v in self.statpay.items():
                    aero.statMath(k,v)
                
        
        
                