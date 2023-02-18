class Solution(object):
    def longestPalindrome(self,s) :
        res = [  s[i: j]  for i in range(len(s)) for j in range(i + 1, len(s) + 1) if  s[i: j] ==  s[i: j][::-1]]
        pal = {}
        
        #print(a_dict)
        for palabra in res:
            pal[palabra] = len(palabra)
        #print(pal)       
        #print(max(pal.values()))
        max_value = max(pal, key=pal.get)
        return max_value
        
        
                
   
   

w=Solution().longestPalindrome("fkyidosnupvunmklebjiepwdmfhqjfjgtcdivzgibcewxviirtneumvhcwzvstvtnzrnzknehahdipswtvgmqhmexnjtqcpngvojdxmhwqhrdcgybehvrfsqkroaztrhyeuuzkthfhwtbfnyghlzjqsqjpqvsrkabcxylpgylzzgyzmhruqyezfcvzcmzzuvtxlbfyukhvnytetagrhsebodddqiowahvflakfkefzlwkdjyxtymypkqkeniriybvdcfnqogilpeiviatavcbtxogxenbfhpfqklrekqefzjunpzrenqhorpqnhxllceubkndibdypbmbjscnryafertbursmghissihgmsrubtrefayrncsjbmbpydbidnkbuecllxhnqprohqnerzpnujzfeqkerlkqfphfbnexgoxtbcvataiviepligoqnfcdvbyirinekqkpymytxyjdkwlzfekfkalfvhawoiqdddobeshrgatetynvhkuyfblxtvuzzmczvcfzeyqurhmzygzzlygplyxcbakrsvqpjqsqjzlhgynfbtwhfhtkzuueyhrtzaorkqsfrvhebygcdrhqwhmxdjovgnpcqtjnxemhqmgvtwspidhahenkznrzntvtsvzwchvmuentriivxwecbigzvidctgjfjqhfmdwpeijbelkmnuvpunsodiykf")
print(w) 
