#include<bits/stdc++.h>
using namespace std;
int solve(string s, int curr,int k,map<pair<int,int>,int> &m)
{
    if(k==0)
    {
        return m[{curr,k}]=curr+1;
    }
    if(curr>=s.size())
    {
        return -1;
    }
    if(m.find({curr,k})!=m.end())
    {
        return m[{curr,k}];
    }
    int maxi=1;
    for(int i=curr+1;i<s.size();i++)
    {
        if(s[i]!=s[curr])
        {
            int x = solve(s,i,k-1,m);
            maxi = max(maxi,x);
        }
    }
    return m[{curr,k}]=maxi;
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string a,b;
        cin>>a>>b;
        if(a==b)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            int a1=0,a2=0,b1=0,b2=0;
            for(int i=0;i<a.size();i++)
            {
                if(a[i]=='0')
                {
                    a1++;
                }
                else
                {
                    a2++;
                }
                if(b[i]=='0')
                {
                    b1++;
                }
                else
                {
                    b2++;
                }
            }
            if(b2 && b1)
            {
                cout<<"YES"<<endl;
            }
            else
            {
                cout<<"NO"<<endl;
            }
        }
    }
}