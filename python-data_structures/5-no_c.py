#!/usr/bin/python3sdef no_c(my_string):    new_string = ""    for i in range(len(my_string)):        element = my_string[i]                if element.lower() not in ('c'):            new_string += element                return new_string