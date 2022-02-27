from column_slice import ColumnSlice

class Slicer():
    def __init__(self, xlen, pixel_array, colum_order) -> None:
        self.__colum_order = colum_order
        self.__pixel_array = pixel_array
        self.__xlen = xlen
        
    def col_slice_gen(self):
        counter = 0
        while counter-1!=self.__xlen-1:
            counter+=1
            if counter < self.__xlen-1:
                yield ColumnSlice(self.__pixel_array[self.__colum_order[counter]:self.__colum_order[counter+1], ::], 550+counter, 100)
            else:
                yield ColumnSlice(self.__pixel_array[self.__colum_order[self.__xlen-1]:, ::], 550+self.__xlen-1, 100)

    def draw_slices(self, screen):
        for element in self.col_slice_gen():
            if 1000-element.get_col_surface_rect.x >=0:
                screen.blit(element.get_column_surface, element.get_col_surface_rect)

    def close(self):
        self.__pixel_array.close()