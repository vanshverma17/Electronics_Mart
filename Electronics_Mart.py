def intro():
    print('*'*157)
    print('')
    print('The ElectronicMart'.center(157))
    print(' ________'.center(157))
    print('| ______ |'.center(157))
    print('||      ||'.center(157))
    print('||      ||'.center(157))
    print('||      ||'.center(157))
    print('||      ||'.center(157))
    print('||      ||'.center(157))
    print('||[][][]||'.center(157))
    print('||______||'.center(157))
    print('|________|'.center(157))
    print('')
    print('  !Get your favourite gadgets at one place!  '.center(157))
    print('')
    print('')
    print('*'*157)


    
def modify_LAP():
    idd =  int(input(' '*50+'Enter ID of the product you want to MODIFY: '))
    cur.execute('select * from laptop where id={}'.format(idd))
    print('_'*157)
    print('')
    print('DETAILS'.center(157))
    print('_'*157)
    print(tabulate(cur.fetchall(),headers=['ID','Nsme','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specs'],tablefmt='fancy_grid'))
    val=''
    name = input(' '*50+'Enter Name : ')
    if name:
        up_value='name="{}"'.format(name)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value
            
    brand = input(' '*50+'Enter Brand : ')
    if brand:
        up_value='brand="{}"'.format(brand)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value
    
    price = int(input(' '*50+'Enter Price : '))
    if price:
        up_value='price={}'.format(price)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value
            
    proc = input(' '*50+'Enter Processor Details : ')
    if proc:
        up_value='processor="{}"'.format(proc)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value

    ram = input(' '*50+'Enter RAM Details : ')
    if ram:
        up_value='ram="{}"'.format(ram)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value
            
    rom = input(' '*50+'Enter ROM Details : ')
    if rom:
        up_value='rom="{}"'.format(rom)
        if val=='':
            val=up_value
        else:
            val=val+','+up_value
            
    graphics = input(' '*50+'Enter GPU Details : ')
    if graphics:
        up_value='graphics="{}"'.format(graphics)
        if values=='':
            values=up_values
        else:
            values=values+','+up_value
            
    other_specs = input(' '*50+'Enter other Specifications : ')
    if other_specs:
        up_value='other_specifications="{}"'.format(other_specs)
        if values=='':
            values=up_values
        else:
            values=values+','+up_value
    query = 'update laptop set {} where id={}'.format(val,idd)
    cur.execute(query)
    a.commit()
    print(cur.
          rowcount,'record updated')
   
def modify_PHN():
    idd =  int(input(' '*50+'Enter ID of the product you want to MODIFY: '))
    cur.execute('select * from phone where id={}'.format(idd))
    print('_'*157)
    print('')
    print('DETAILS'.center(157))
    print('_'*157)
    print(tabulate(cur.fetchall(),headers=['ID','Nsme','Brand','Price','Processor','storage','OS','screen size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid'))
    val=''
    name = input(' '*50+'Enter Name : ')
    if name:
        up_val='name="{}"'.format(name)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    brand = input(' '*50+'Enter Brand : ')
    if brand:
        up_val='brand="{}"'.format(brand)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
    
    price = int(input(' '*50+'Enter Price : '))
    if price:
        up_val='price={}'.format(price)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    proc = input(' '*50+'Enter Processor Details : ')
    if proc:
        up_val='processor="{}"'.format(proc)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    stor = input(' '*50+'Enter storage Details : ')
    if stor:
        up_val='storage="{}"'.format(stor)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    os = input(' '*50+'Enter Operating System : ')
    if os:
        up_val='os="{}"'.format(os)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    s_s = input(' '*50+'Enter screen size : ')
    if s_s:
        up_val='screen_size="{}"'.format(s_s)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
    battery = input(' '*50+'Enter Battery Details : ')       
    if battery:
        up_val='battery="{}"'.format(battery)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    cam = input(' '*50+'Enter Camera Details : ')       
    if cam:
        up_val='camera="{}"'.format(cam)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val

    other_specs = input(' '*50+'Enter Other Specifications : ')       
    if other_specs:
        up_val='other_specifications="{}"'.format(other_specs)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    query = 'update phone set {} where id={}'.format(val,idd)
    cur.execute(query)
    a.commit()
    print(cur.
          rowcount,'record updated')
    
def modify_TV():

    idd =  int(input(' '*50+'Enter ID of the product you want to MODIFY: '))
    cur.execute('select * from tv where id={}'.format(idd))
    print('_'*157)
    print('')
    print('DETAILS'.center(157))
    print('_'*157)
    print(tabulate(cur.fetchall(),headers=['ID','Nsme','Brand','Display','Features','Connectivity','TV_type','Other_specs','Price'],tablefmt='fancy_grid'))
    val=''

    name = input(' '*50+'Enter Name : ')
    if name:
        up_val='name="{}"'.format(name)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val

    brand = input(' '*50+'Enter Brand : ')
    if brand:
        up_val='brand="{}"'.format(brand)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
    
    dis = input(' '*50+'Enter display Details : ')
    if dis:
        up_val='display="{}"'.format(dis)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    feat = input(' '*50+'Enter Features : ')
    if feat:
        up_val='features="{}"'.format(feat)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val

    connect = input(' '*50+'Enter Connectivity Details : ')
    if connect:
        up_val='connectivity="{}"'.format(connect)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    tv_type = input(' '*50+'Enter TV TYPE : ')
    if tv_type:
        up_val='tv_type="{}"'.format(tv_type)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    other_specs = input(' '*50+'Enter Other Specs : ')
    if other_specs:
        up_val='other_specs="{}"'.format(other_specs)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
            
    price = int(input(' '*50+'Enter Price : '))
    if price:
        up_val='price={}'.format(price)
        if val=='':
            val=up_val
        else:
            val=val+','+up_val
    query = 'update tv set {} where id={}'.format(val,idd)
    cur.execute(query)
    a.commit()
    print(cur.rowcount,'record updated')

def delete_LAP():
    query = 'select * from laptop'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('LAPTOPS'.center(157))
    print('_'*157)
    print(x)
    idd = int(input('Enter Product ID of the laptop you want to delete : '))
    query = 'delete from laptop where id='+str(idd)
    confirm = input('Are you sure you want to delete?(Y/N) : ')
    if confirm.lower()=='y':
        cur.execute(query)
        a.commit()
        print(cur.rowcount,'Record Deleted')
    elif confirm.lower()=='n':
        exit()
    else:
        print('Enter a suitable character!')
        delete_LAP()

def delete_PHN():
    query = 'select * from phone'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','Storage','OS','Screen Size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('PHONES'.center(157))
    print('_'*157)
    print(x)
    idd = int(input('Enter Product ID of Phone you want to delete : '))
    query = 'delete from phone where id='+str(idd)
    confirm = input('Are you sure you want to delete?(Y/N) : ')
    if confirm.lower()=='y':
        cur.execute(query)
        a.commit()
        print(cur.rowcount,'Record Deleted')
    elif confirm.lower()=='n':
        exit()
    else:
        print('Enter a suitable character!')
        delete_PHN()
        
def delete_TV():
    query = 'select * from tv'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('TELEVISIONS'.center(157))
    print('_'*157)
    print(x)
    idd = int(input('Enter Product ID of Television you want to DELETE from the RECORDS : '))
    query = 'delete from tv where id='+str(idd)
    confirm = input('Are you sure you want to delete?(Y/N) : ')
    if confirm.lower()=='y':
        cur.execute(query)
        a.commit()
        print(cur.rowcount,'Record Deleted')
    elif confirm.lower()=='n':
        delete_TV()
    else:
        print('Enter a suitable character!')
        delete_LAP()

def showall_LAP():
    query = 'select * from laptop'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('LAPTOPS'.center(157))
    print('_'*157)
    print(x)

def showall_PHN():
    query = 'select * from phone'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','Storage','OS','Screen Size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('PHONES'.center(157))
    print('_'*157)
    print(x)

def showall_TV():
    query = 'select * from tv'
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
    print('_'*157)
    print('')
    print('TELEVISIONS'.center(157))
    print('_'*157)
    print(x)

def insert_LAP():
    print('-'*157)
    print('')
    print('ENTER THE DETAILS OF THE LAPTOP'.center(157))
    print('')
    print('-'*157)
    iid = int(input(' '*50+'Enter Product ID : '))
    name = input(' '*50+'Enter Name : ')
    brand = input(' '*50+'Enter Brand : ')
    price = int(input(' '*50+'Enter Price : '))
    proc = input(' '*50+'Enter Processor Details : ')
    ram = input(' '*50+'Enter RAM Details : ')
    rom = input(' '*50+'Enter ROM Details : ')
    graphics = input(' '*50+'Enter GPU Details : ')
    other_specs = input(' '*50+'Enter other Specifications : ')
    print('')
    print('-'*157)
    rec = (iid,name,brand,price,proc,ram,rom,graphics,other_specs)
    query = 'insert into laptop values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(query,rec)
    a.commit()
    print(cur.rowcount,'Record Added')

def insert_PHN():
    print('-'*157)
    print('')
    print('ENTER THE DETAILS OF THE PHONE'.center(157))
    print('')
    print('-'*157)
    iid = int(input(' '*50+'Enter Product ID :'))
    name = input(' '*50+'Enter Name : ')
    brand = input(' '*50+'Enter Brand : ')
    price = int(input(' '*50+'Enter Price : '))
    proc = input(' '*50+'Enter Processor Details : ')
    storage = input(' '*50+'Enter Storage Details : ')
    os = input(' '*50+'Enter Operating System : ')
    ss = input(' '*50+'Enter Screen Size : ')
    battery = input(' '*50+'Enter Battery Details : ')
    camera = input(' '*50+'Enter Camera Details : ')
    other_specs = input(' '*50+'Enter other specifications : ')
    print('')
    print('-'*157)
    rec = (iid,name,brand,price,proc,storage,os,ss,battery,camera,other_specs)
    query = 'insert into phone values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(query,rec)
    a.commit()
    print(cur.rowcount,'Record Added')

def insert_TV():
    print('-'*157)
    print('')
    print('ENTER THE DETAILS OF THE TELEVISION'.center(157))
    print('')
    print('-'*157)
    iid = int(input(' '*50+'Enter Product ID :'))
    name = input(' '*50+'Enter Name : ')
    brand = input(' '*50+'Enter Brand : ')
    dis = input(' '*50+'Enter Display Details : ')
    feat = input(' '*50+'Enter Features : ')
    connect = input(' '*50+'Enter Connectivity Details : ')
    tv_type = input(' '*50+'Enter TV Type : ')
    other_specs = input(' '*50+'Enter Other_Specs : ')
    price = int(input(' '*50+'Enter Price : '))
    print('')
    print('-'*157)
    rec = (iid,name,brand,dis,feat,connect,tv_type,other_specs,price)
    query = 'insert into tv values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(query,rec)
    a.commit()
    print(cur.rowcount,'Record Added')


    
    
        
            
            


def sortby_LAP():
    print('_'*157)
    print('')
    print('Compare Laptop'.center(157))
    print('')
    print('_'*157)
    print('Brand  :  1 '.center(157))
    print('Price Range : 2'.center(157))
    print('RAM : 3'.center(157))
    
    opt = int(input('Select The Category to Compare : '.center(157)))
    
    if opt==1:
        print('')
        print('_'*157)
        print('')
        print(' '*50+'SELECT THE BRAND(lenovo,asus,dell,hp)')
        print('')
        brand = input(' '*50+'enter the name of the brand : ')
        rec1 = [brand]
        query1 = 'select * from laptop where brand=%s'
        cur.execute(query1,rec1)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_')
        
    elif opt==2:
        print('')
        print('_'*157)
        print('')
        print('ENTER THE PRICE RANGE'.center(157))
        print('')
        firstp = int(input('Enter the LOWER LIMIT of your PRICE limit : '.center(157)))
        secondp = int(input('Enter the UPPER LIMIT of your PRICE limit : '.center(157)))
        
        query2 = 'select * from laptop where price>='+str(firstp)+' and price<='+str(secondp)
        cur.execute(query2)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
    elif opt==3:
        print('')
        print('_'*157)
        print('')
        print('select the RAM'.center(157))
        ram = int(input('enter the RAM : '.center(157)))
        query3='select * from laptop where ram='+str(ram)
        cur.execute(query3)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)

def sortby_PHN():
    print('_'*157)
    print('')
    print('Compare PHONE'.center(157))
    print('')
    print('_'*157)
    print('BRAND  :  1 '.center(157))
    print('PRICE RANGE : 2'.center(157))
    
    
    opt = int(input('Select The Category to Compare : '.center(157)))
    
    if opt==1:
        print('')
        print('_'*157)
        print('')
        print(' '*50+'SELECT THE BRAND(motorola,oneplus,samsung,apple)')
        print('')
        brand = input(' '*50+'enter the name of the brand : ')
        rec1 = [brand]
        query1 = 'select * from phone where brand=%s'
        cur.execute(query1,rec1)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','Storage','OS','Screen Size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
        sortby_PHN()
        
    elif opt==2:
        print('')
        print('_'*157)
        print('')
        print('ENTER THE PRICE RANGE'.center(157))
        print('')
        firstp = int(input(' '*50+'Enter the LOWER LIMIT of your PRICE limit : '))
        secondp = int(input(' '*50+'Enter the UPPER LIMIT of your PRICE limit : '))
        
        query2 = 'select * from phone where price>='+str(firstp)+' and price<='+str(secondp)
        cur.execute(query2)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','Storage','OS','Screen Size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
        sortby_PHN()

def sortby_TV():
    print('_'*157)
    print('')
    print('Compare TELEVISION'.center(157))
    print('')
    print('_'*157)
    print('BRAND  :  1 '.center(157))
    print('PRICE RANGE : 2'.center(157))
    print('DISPLAY SIZE : 3'.center(157))
    
    
    opt = int(input(' '*50+'Select The Category to Compare : '))
    
    if opt==1:
        print('')
        print('_'*157)
        print('')
        print(' '*50+'SELECT THE BRAND(sony,samsung)')
        print('')
        brand = input(' '*50+'enter the name of the brand : ')
        rec1 = [brand]
        query1 = 'select * from tv where brand=%s'
        cur.execute(query1,rec1)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
        sortby_TV()
        
    elif opt==2:
        print('')
        print('_'*157)
        print('')
        print('ENTER THE PRICE RANGE'.center(157))
        print('')
        firstp = int(input(' '*50+'Enter the LOWER LIMIT of your PRICE limit : '))
        secondp = int(input(' '*50+'Enter the UPPER LIMIT of your PRICE limit : '))
        
        query2 = 'select * from tv where price>='+str(firstp)+' and price<='+str(secondp)
        cur.execute(query2)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
        sortby_TV()

    elif opt==3:
        print('')
        print('_'*157)
        print('')
        print('ENTER THE DISPLAY SIZE'.center(157))
        print('')
        display = int(input(' '*50+'Enter the dislay size in inches : '))
        
        query3 = "select * from tv where display like '"+str(display)+"%'"
        cur.execute(query3)
        x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
        print(x)
        print('')
        print('_'*157)
        sortby_TV()

def compare_LAP():
    print('')
    print('_'*157)
    print('')
    print('COMPARE LAPTOP'.center(157))
    print('_'*157)
    print('')
    idd1 = int(input(' '*50+'Enter ID of the first product : '))
    idd2 = int(input(' '*50+'Enter ID of the second product : '))
    query = 'select * from laptop where id='+str(idd1)+' or '+'id='+str(idd2)
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','RAM','ROM','Graphics','Other_Specifications'],tablefmt='fancy_grid')
    print(x)
    print('')
    print('_'*157)
    print('')
    


def compare_PHN():
    print('')
    print('_'*157)
    print('')
    print('COMPARE PHONE'.center(157))
    print('_'*157)
    print('')
    idd1 = int(input(' '*50+'Enter ID of the first product : '))
    idd2 = int(input(' '*50+'Enter ID of the second product : '))
    query = 'select * from phone where id='+str(idd1)+' or '+'id='+str(idd2)
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Price','Processor','Storage','OS','Screen Size','Battery','Camera','Other_Specs'],tablefmt='fancy_grid')
    print(x)
    print('')
    print('_'*157)
    print('')

def compare_TV():
    print('')
    print('_'*157)
    print('')
    print('COMPARE TELEVISION'.center(157))
    print('_'*157)
    print('')
    idd1 = int(input(' '*50+'Enter ID of the first product : '))
    idd2 = int(input(' '*50+'Enter ID of the second product : '))
    query = 'select * from tv where id='+str(idd1)+' or '+'id='+str(idd2)
    cur.execute(query)
    x = tabulate(cur.fetchall(),headers=['ID','Name','Brand','Display','Features','Connectivity','TV_type','Other_Specs','Price'],tablefmt='fancy_grid')
    print(x)
    print('')
    print('_'*157)
    print('')
    
def mainmenu():
    print('_'*157)
    print('')
    print('The ElectronicMart'.center(157))
    print('MainMenu'.center(157))
    print('_'*157)
    print('')
    print('AdminMenu : 1'.center(157))
    print('UserMenu : 2'.center(157))
    print('Exit : 3'.center(157))
    print('')
    option = int(input(" "*63+'choose your option : '))
    print('')
    print('_'*157)
    if option==1:
        AdminMenu()
    elif option==2:
        UserMenu()
        mainmenu()
    elif option==3:
        exit()
    else:
        print('Select a SUITABLE CHOICE!')
        mainmenu()

def UserMenu():
    while True:
        print('_'*157)
        print('')
        print('UserMenu'.center(157))
        print('_'*157)
        print('')
        print('ShowAll : 1'.center(157))
        print('Sort by Categories : 2'.center(157))
        print('Compare Products : 3'.center(157))
        print('BACK : 4'.center(157))
        print('')
        choose=int(input('Choose your option : '))
        if choose==1:
            print('')
            print('_'*157)
            print('_'*157)
            print('')
            print('Enter The Type of Product Below'.center(157))
            print('_'*157)
            print('')
            print('LAPTOPS : 1'.center(157))
            print('PHONES : 2'.center(157))
            print('TELEVISIONS : 3'.center(157))
            print('')
            option = int(input(' '*43+'choose your option : '))   
            print('')
            print('_'*157)
            if option==1:
                showall_LAP()
            elif option==2:
                showall_PHN()
            elif option==3:
                showall_TV()
            else:
                print('Enter a suitable character!')
                UserMenu()
        elif choose==2:
            print('')
            print('_'*157)
            print('_'*157)
            print('')
            print('Enter The Type of Product Below'.center(157))
            print('_'*157)
            print('')
            print('LAPTOPS : 1'.center(157))
            print('PHONES : 2'.center(157))
            print('TELEVISIONS : 3'.center(157))
            print('')
            option = int(input(' '*43+'choose your option : '))   
            print('')
            print('_'*157)
            if option==1:
                sortby_LAP()
            elif option==2:
                sortby_PHN()
            elif option==3:
                sortby_TV()
            else:
                print('Enter a suitable character!')
                UserMenu()
        elif choose==3:
            print('')
            print('_'*157)
            print('_'*157)
            print('')
            print('Enter The Type of Product Below'.center(157))
            print('_'*157)
            print('')
            print('LAPTOPS : 1'.center(157))
            print('PHONES : 2'.center(157))
            print('TELEVISIONS : 3'.center(157))
            print('')
            option = int(input(' '*43+'choose your option : '))   
            print('')
            print('_'*157)
            if option==1:
                compare_LAP()
            elif option==2:
                compare_PHN()
            elif option==3:
                compare_TV()
            else:
                print('Enter a suitable character!')
                UserMenu()
        elif choose==4:
            mainmenu()

def AdminMenu():
    while True:
        print('_'*157)
        print('')
        print('AdminMenu'.center(157))
        print('_'*157)
        print('')
        print('Insert Product : 1'.center(157))
        print('Delete product  : 2'.center(157))
        print('Edit Product : 3'.center(157))
        print('Show All : 4'.center(157))
        print('BACK : 5'.center(157))
        print('')
        opt = int(input(' '*43+'choose your option : '))
        if opt==5:
            mainmenu()
        
        print('')
        print('_'*157)
        print('_'*157)
        print('')
        print('Enter The Type of Product Below'.center(157))
        print('_'*157)
        print('')
        print('LAPTOPS : 1'.center(157))
        print('PHONES : 2'.center(157))
        print('TELEVISIONS : 3'.center(157))
        print('')
        option = int(input(' '*43+'choose your option : '))   
        print('')
        print('_'*157)
        if opt==1 and option==1:
            insert_LAP()
        elif opt==1 and option==2:
            insert_PHN()
        elif opt==1 and option==3:
            insert_TV()
        elif opt==2 and option==1:
            delete_LAP()
        elif opt==2 and option==2:
            delete_PHN()
        elif opt==2 and option==3:
            delete_TV()
        elif opt==3 and option==1:
            modify_LAP()
        elif opt==3 and option==2:
            modify_PHN()
        elif opt==3 and option==3:
            modify_TV()
        elif opt==4 and option==1:
            showall_LAP()
        elif opt==4 and option==2:
            showall_PHN()
        elif opt==4 and option==3:
            showall_TV()
        elif choose==3:
            mainmenu()
        
import mysql.connector
from tabulate import tabulate
global a
a = mysql.connector.connect(host='localhost',user='root',password='vansh@174',database='electronic_mart')
cur = a.cursor()
intro()
mainmenu()
    
        

