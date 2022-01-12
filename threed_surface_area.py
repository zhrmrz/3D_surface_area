class Sol:
    def threed_surface_area(self,grid):
        n=len(grid)
        surface=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                surface+=grid[i][j]*4+2
                if i!=0:
                    surface-= 2*min(grid[i][j],grid[i-1][j])
                if j!=0:
                    surface -= 2*min(grid[i][j], grid[i][j-1])
                print(surface)

        return surface

if __name__ == '__main__':
    p = Sol()
    print(p.threed_surface_area(grid =[[2,2,2],[2,1,2],[2,2,2]]))
