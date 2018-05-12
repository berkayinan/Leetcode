class Tensor:
    def __init__(self,*dims):
        self.shape=dims
        if len(dims)==1:
            self.container=[0 for _ in range(dims[0])]
        else:
            self.container=[Tensor(*dims[1:]) for _ in range(dims[0])]

    def __getitem__(self,idx):
        if len(idx)==1:
            return self.container[idx[0]]
        return self.container[idx[0]].__getitem__(idx[1:])
    
    def __setitem__(self,idx,val):
        if len(idx)==1:
            self.container[idx[0]]=val
        else:
            self.container[idx[0]].__setitem__(idx[1:],val)

def main():
    my_tensor=Tensor(2,2)
    my_tensor[0,0]=5
    print(my_tensor[0,0])

if __name__ == '__main__':
    main()
