import CellPhoneClass as c

def main():
    #get input data

    manu = input("Enter manufacturer: ")
    mode = input("Enter model: ")
    retail = input("Enter retail price: ")

    #create instance of cell phone class
    phone = c.CellPhone(manu,mode,retail)

    print("Here is the data you entered")
    print("Manufacturer:", phone.get_manufact())
    print("Model Number:", phone.get_model())
    print("Retail Price: $",phone.get_retail_price())

main()
