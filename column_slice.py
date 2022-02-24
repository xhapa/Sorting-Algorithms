import pygame

class ColumnSlice():
    def __init__(self, pixel_array: pygame.PixelArray, posx: int, posy: int) -> None:
        self.__column_surface = pixel_array.make_surface()
        self.__col_surface_rect = self.__column_surface.get_rect() 
        self.__col_surface_rect.x = posx
        self.__col_surface_rect.y = posy

    @property
    def get_column_surface(self):
        return self.__column_surface

    @property
    def get_col_surface_rect(self):
        return self.__col_surface_rect