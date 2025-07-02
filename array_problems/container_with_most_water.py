def maxArea(height):
    n = len(height)
    max_area = 0
    for i in range(n-1):
        for j in range(i+1,n):
            h = min(height[i],height[j])
            w = j - i
            area = h * w
            if area > max_area:
                max_area = area
            

    return max_area

height = [1,8,6,2,5,4,8,3,7];
result = maxArea(height)
print(result)