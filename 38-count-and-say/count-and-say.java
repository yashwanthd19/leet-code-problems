class Solution {
    public String countAndSay(int n) {
        String a="1";
       
        while(n>1){
             StringBuilder b=new StringBuilder();
            for(int i=0;i<a.length();)
            {
                int count=1;
                
                while(i+1<a.length()&& a.charAt(i)==a.charAt(i+1))
                {
                    count++;
                    i++;

                }
                b.append(count).append(a.charAt(i));
                i++;

            }
            a=b.toString();
            n--;


        }
        
        return a;
        
        
    }
}