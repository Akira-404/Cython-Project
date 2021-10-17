double cfib(int n)
{
    int i;
    double a=0.0,b=1.0,temp;
    for(i=1;i<n;i++)
    {
       temp=a;
       a=a+b;
       b=temp;
    }
    return a;
}
