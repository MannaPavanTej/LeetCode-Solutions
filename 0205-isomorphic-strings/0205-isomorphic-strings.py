class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        for cs,ct in zip(s,t):
            if cs in st and st[cs]!=ct:
                return False
            if ct in ts and ts[ct]!=cs:
                return False
            st[cs]=ct
            ts[ct]=cs

        return True