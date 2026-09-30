class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int n=seq.length();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=(i^seq.charAt(i))&1;

        }
        return a;
        
    }
}