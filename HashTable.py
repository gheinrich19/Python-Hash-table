# This is my hash program!
class MyHashTable:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.fruits = [None] * self.size
        
        
  
    
    # This insert function takes a key and fruit value to insert into two list. they will map tp eachother and the key is hashed using 
    # The hashFunction() which is just mod 10 
    
    def insert(self, key, fruitData):
        # This variable holds the hashed value of the key
        itsHashed = self.hashFunction(key, len(self.keys))
        
        #This is where we initialize the the lists and add the new data to them 
        if self.keys[itsHashed] == None:
            self.keys[itsHashed] = itsHashed
            self.fruits[itsHashed] = fruitData
        else:
        # Checking to see if the data has been changed according to the same hashed value
            if self.keys[itsHashed] == key:
                self.data = fruitData
            
            # this is where we do our linear probing and use the rehash function
            else:
                newHash = self.reHash(itsHashed, len(self.keys))
                
                while self.keys[newHash] != None and self.keys[newHash] != key:
                    newHash = self.reHash(newHash,len(self.keys))
                    
                if self.keys[newHash] == None:
                    self.keys[newHash] = key
                    self.fruits[newHash] = fruitData
                    
                else:
                    self.fruits = fruitData
                    
    def hashFunction(self, key,size):
        return key%10
        
    def reHash(self, oldHash, size):
        return(oldHash+1)%size           
        
def main():
    
    tablbesize = 10
    H = MyHashTable()
    hashval = H.hashFunction(5,tablbesize)
    print(hashval)
    
    H.insert(5, "bananna")
    
    print H.fruits
    print H.keys
    
    H.insert(15, "grapes")
    
    #for val in H.fruits: print val
    
    print H.fruits[H.hashFunction(5,tablbesize)]
    
    print H.fruits
    print H.keys
        
if __name__=="__main__":main()