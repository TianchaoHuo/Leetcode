class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) 
    {
        if(nums.size() < 2 )
            return nums.size();
        static const int begin = 0;
        static const int up = 1;
        static const int down = 2;
        int state = begin;
        int max_length = 1;
        
        for (int i=1; i<nums.size(); i++)
        {
            switch(state)
            {
                case begin:
                    if(nums[i-1]<nums[i])
                    {
                        state = up;
                        max_length++;
                    }
                    else if (nums[i-1]>nums[i])
                    {
                        state = down;
                        max_length++;
                    }
                    break;
                case up:
                    if(nums[i-1]>nums[i])
                    {      
                       state = down;
                       max_length++;
                    }
                    break;
                case down:
                    if (nums[i-1]<nums[i])
                    {
                        state = up;
                        max_length++;
                    }
                    break;
            }
        }
        return max_length;
    }
};