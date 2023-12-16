def time_conversion(str):
      if str[-2:] == "AM" and str[:2] == "12":
         return "00" + str[2:-2]
      elif str[-2:] == "AM":
         return str[:-2]
      elif str[-2:] == "PM" and str[:2] == "12":
         return str[:-2]
      else:
         return str(int(str[:2]) + 12) + str[2:8]   