class Calculator:
    #class
    def baseNtobase10(self, userval='0', base='0', noInput=False):
        if noInput == False:
            print("")
            print("\t\tConvert base N to base 10!")
            userval = input("\t\tPlease enter a number: ")
            base = input("\t\t[N] Please provide a base: ")

        chars = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        char_vals = {'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15,'G': 16,'H': 17,'I': 18,'J': 19,'K': 20,'L': 21,'M': 22,'N': 23,'O': 24,'P': 25,'Q': 26,'R': 27,'S': 28,'T': 29,'U': 30,'V': 31,'W': 32,'X': 33,'Y': 34,'Z': 35}
        val = userval.split('.', 1)

        negative = False
        if val[0][0] == '-': 
            val[0] = val[0][1:]
            negative = True

        try:
            base = int(base)
            if base == 10 and int(userval) >= 0: return str(userval)
            a, b, c = 0, 0, -1
            for i, z in enumerate(val[0][::-1]):
                if z in chars: 
                    if char_vals[z] <= base-1: a += char_vals[z] * (base ** i)
                    else: 
                        print("")
                        print("\t\t[Error] base {} does not allow char {}".format(base, char_vals[z]))
                        print("\t\tPlease try again")
                        if noInput: return self.binarySimpleCalc()
                        return self.baseNtobase10()
                else: 
                    if int(z) >= 0 and int(z) < base: a += int(z) * (base ** i)
                    else:
                        print("")
                        print("\t\t[Error] base {} does not allow number {}".format(base, int(z)))
                        print("\t\tPlease try again")
                        if noInput: return self.binarySimpleCalc()
                        return self.baseNtobase10()  
        
            if len(val) == 1: 
                print("")
                if negative: return str(a * -1)
                return str(a)
        
            for z in val[1]:
                if z in chars: 
                    if char_vals[z] <= base-1: b += char_vals[z] * (base ** c)
                    else: 
                        print("")
                        print("\t\t[Error] base {} does not allow char {}".format(base, char_vals[z]))
                        print("\t\tPlease try again")
                        if noInput: return self.binarySimpleCalc()
                        return self.baseNtobase10()
                else: 
                    if int(z) >= 0 and int(z) < base: b += int(z) * (base ** c)
                    else:
                        print("")
                        print("\t\t[Error] base {} does not allow number {}".format(base, int(z)))
                        print("\t\tPlease try again")
                        if noInput: return self.binarySimpleCalc()
                        return self.baseNtobase10()  
                c -= 1
        
            if negative: return str((a+b) * -1)
            
            print("")
            return str(a+b)
    
        except:
            print("")
            print("\t\t[Error] You did not provide a valid number!")
            print("\t\tPlease try again")
            if noInput: return self.binarySimpleCalc()
            return self.baseNtobase10()

    def base10tobaseN(self, userval='0', base='0', noInput=False):
        if noInput == False:
            print("")
            print("\t\tConvert base 10 to base N!")
            userval = input("\t\tPlease enter a number: ")
            base = input("\t\t[N] Please provide a base: ")

        chars = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
        char_vals = {'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15,'G': 16,'H': 17,'I': 18,'J': 19,'K': 20,'L': 21,'M': 22,'N': 23,'O': 24,'P': 25,'Q': 26,'R': 27,'S': 28,'T': 29,'U': 30,'V': 31,'W': 32,'X': 33,'Y': 34,'Z': 35}

        val = userval.split('.', 1)
        if len(val) > 1: 
            print("")
            print("\t\t[Error] converter does not allow for decimal point")
            print("\t\tPlease try again")
            if noInput: return self.binarySimpleCalc()
            return self.base10tobaseN()

        try:
            base = int(base)
            userval = int(userval)
            if base == 10: return str(userval)
            if userval < 0: 
                print("\t\t[Error] No negative numbers please")
                if noInput: return self.binarySimpleCalc()
                return self.base10tobaseN()
            new_val = userval
            final = []
            while new_val >= base:
                aux = new_val / base
                new_val = int(aux) 
                temp = aux - new_val
                temp *= base 
                temp = int(temp)
                if temp in char_vals.values():
                    key = [k for k, v in char_vals.items() if v == temp]
                    temp = key[0]
                final.append(temp)
        
            if new_val in char_vals.values():
                key = [k for k, v in char_vals.items() if v == new_val]
                new_val = key[0]
                final.append(new_val)
            else:
                if new_val != 0: final.append(new_val)
            val = ''
            for z in final[::-1]:
                val += str(z)

            print("")
            return val

        except:
            print("")
            print("\t\t[Error] You did not provide a valid number!")
            print("\t\tPlease try again")
            if noInput: return self.binarySimpleCalc()
            return self.base10tobaseN()

    def binarySimpleCalc(self, operation=1):
        if operation == 1:
            print("")
            print("\t\tBinary addition!")

        if operation == 0:
            print("")
            print("\t\tBinary subtraction!")
    
        valA = input("\t\tPlease enter number A: ")
        valB = input("\t\tPlease enter number B: ")
    
        valAt = valA.split('.', 1)
        valBt = valB.split('.', 1)
        if len(valAt) > 1 or len(valBt) > 1: 
            print("")
            print("\t\t[Error] converter does not allow for decimal point")
            print("\t\tPlease try again")
            return self.binarySimpleCalc(operation)

        valA = self.baseNtobase10(userval=str(valA), base=2, noInput=True)
        valB = self.baseNtobase10(userval=str(valB), base=2, noInput=True)
        valA, valB = int(valA), int(valB)
        final = 0
        if operation == 1: final = valA + valB
        else: final = valA - valB
        final = self.base10tobaseN(userval=str(final), base=2, noInput=True)
        
        print("")
        return final

    def onescomplement(self, userA='', noInput=False):
        if noInput == False:
            print("")
            print("\t\tObtain 1's complement of binary number!")
            userA = input("\t\tPlease enter number A: ")

        valA = userA.split('.', 1)
        if len(valA) > 1: 
            print("")
            print("\t\t[Error] converter does not allow for decimal point")
            print("\t\tPlease try again")
            return self.onescomplement()

        listA = []
        try:
            for a in userA:
                if int(a) != 1 and int(a) != 0: 
                    print("")
                    print("\t\t[Error] not a binary number!")
                    print("\t\tplease try again")
                    return self.onescomplement() 
                listA.append(a)
        except:
            print("")
            print("\t\t[Error] not a binary number!")
            print("\t\tplease try again")
            return self.onescomplement() 

        for i in range(len(listA)):
            if int(listA[i]) == 1: listA[i] = 0
            else: listA[i] = 1

        final = ''
        for z in listA:
            final += str(z)

        print("")
        return final 
    
    def twoscomplement(self):
        print("")
        print("\t\tObtain 2's complement of binary number!")
        userA = input("\t\tPlease enter number A: ")

        valA = userA.split('.', 1)
        if len(valA) > 1: 
            print("")
            print("\t\t[Error] converter does not allow for decimal point")
            print("\t\tPlease try again")
            return self.twoscomplement()

        try:
            for a in userA:
                if int(a) != 1 and int(a) != 0: 
                    print("")
                    print("\t\t[Error] not a binary number!")
                    print("\t\tplease try again")
                    return self.twoscomplement() 
      
        except:
            print("")
            print("\t\t[Error] not a binary number!")
            print("\t\tplease try again")
            return self.twoscomplement()

        final = self.onescomplement(userA, True) 
        final = [int(z) for z in final]
        pass1 = False
        for i in range(len(final)-1,-1,-1):
            if final[i] == 0:
                if pass1: 
                    final[i] = 1
                    pass1 = False
                elif i == len(final)-1:
                    final[i] = 1 
            elif final[i] == 1:
                if pass1:
                    final[i] = 0
                    pass1 = True
                elif i == len(final)-1:
                    final[i] = 0
                    pass1 = True
        if pass1: final.insert(0,1)                   
        final2 = ''
        for z in final:
            final2 += str(z)

        print("")
        return final2
    
    def signedmagnitude(self):
        print("")
        print("\t\tObtain signed magnitude of binary number!")
        userA = input("\t\tPlease enter number A: ")

        valA = userA.split('.', 1)
        if len(valA) > 1: 
            print("")
            print("\t\t[Error] converter does not allow for decimal point")
            print("\t\tPlease try again")
            return self.signedmagnitude()

        listA = []
        try:
            for a in userA:
                if int(a) != 1 and int(a) != 0: 
                    print("")
                    print("\t\t[Error] not a binary number!")
                    print("\t\tplease try again")
                    return self.signedmagnitude()
                listA.append(a)
        except:
            print("")
            print("\t\t[Error] not a binary number!")
            print("\t\tplease try again")
            return self.signedmagnitude()

        if int(listA[0]) == 0: listA[0] = 1
        else: listA[0] = 0

        final = ''
        for z in listA:
            final += str(z)

        print("")
        return final