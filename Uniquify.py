class Tensor():
    def __init__(self, data, shape):
        self.data=data
        self.shape=shape
        self.tensor=self.shape_data()
    
    def shape_data(self):
        if self.shape == []:
            return []
        total_element_num=1
        for i in self.shape:
            total_element_num *= i
        
        if len(self.shape) >= total_element_num:
            self.data = self.data[:total_element_num]
        else:
            self.data = self.data+[0 for _ in range(total_element_num-len(self.data))]       
     
        temp=self.data
        
        for i in range(len(self.shape),0,-1):
            
            temp=self.make_array(self.shape[i-1],temp)
            
        return temp[0]
    
    
    def make_array(self, arr_size, arr):
        temp=[]
        for i in range(0, len(arr), arr_size):
            t=arr[i:i+arr_size]
            temp.append(t)
        return temp

t = Tensor([0,1,2,3,4,5,0.1,0.2,-3], [2,3,2])
print(t.tensor)

t = Tensor([0,1,2,3,4,5,0.1,0.2,-3,-2,-1,3,2,1], [5,2])
print(t.tensor)
