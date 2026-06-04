class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        s1,s2=str(num1),str(num2)
        peak=valley=0
        if(len(s1)<=2 and len(s2)<=2):
            return 0
        
        else:
            for i in range(num1,num2+1):
                s=str(i)
                for j in range(1, len(s) - 1):
                    if(int(s[j-1])<int(s[j])>int(s[j+1])):
                        peak+=1
                    elif(int(s[j-1])>int(s[j])<int(s[j+1])):
                        valley+=1
                
            return (peak+valley)

        