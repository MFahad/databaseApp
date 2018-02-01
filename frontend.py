""""
BookStore
made by Muhammad Fahad

"""

from tkinter import *
from backend import Database 

backend=Database("books.db")#creating database object

##############################binding function to get the selected item as tuple#########################
def get_selected_row(event): #binding function 
	try:		#since when the program executes the list is empty hence it throws an error
		global selected_tuple
		index=list_book.curselection()[0] #to select the first element tuple
		print(index)
		selected_tuple=list_book.get(index) #from the listbox get the tuple with the index 
		print(selected_tuple)
		#printing the variables selected in the entries
		en1.delete(0,END)
		en1.insert(END,selected_tuple[1])
		en2.delete(0,END)
		en2.insert(END,selected_tuple[2])
		en3.delete(0,END)
		en3.insert(END,selected_tuple[3])
		en4.delete(0,END)
		en4.insert(END,selected_tuple[4])
	except IndexError:
		pass #the program generates index error whenever list is empty and user tries to select it, so pass does nothing when there is a empty listbox

#############################building wrapper functions#######################################
def view_command():
	list_book.delete(0,END)
	for row in backend.view():
		list_book.insert(END,row)#the new rows will be put at the END of the list box
		
def search_command():
	list_book.delete(0,END)
	for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()): #appending the get method bcs we need to take variable as string
		list_book.insert(END,row)

def add_command():
	backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	list_book.delete(0,END)
	list_book.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())) #just displaying the user input in the list box not from database
	
def delete_command():
	backend.delete(selected_tuple[0]) #here [0] is the postion of the id which is the only element needed by the delete function
	
def update_command():
	backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	

	
window=Tk() #creates the main window
window.wm_title("Bookstore")		#title

#########################4 lablels title author year and ISBN###########################

lb_title=Label(window,text="Title") 
lb_title.grid(row=0,column=0)

lb_author=Label(window,text="Author") 
lb_author.grid(row=0,column=2)

lb_year=Label(window,text="Year") 
lb_year.grid(row=1,column=0)

lb_isbn=Label(window,text="ISBN") 
lb_isbn.grid(row=1,column=2)

############################4 entries for each label	#################################
title_text=StringVar() #funtion that creates the object which will take user input
en1=Entry(window,textvariable=title_text)
en1.grid(row=0,column=1)

author_text=StringVar() #funtion that creates the object which will take user input
en2=Entry(window,textvariable=author_text)
en2.grid(row=0,column=3)

year_text=StringVar() #funtion that creates the object which will take user input
en3=Entry(window,textvariable=year_text)
en3.grid(row=1,column=1)

isbn_text=StringVar() #funtion that creates the object which will take user input
en4=Entry(window,textvariable=isbn_text)
en4.grid(row=1,column=3)

##########################listbox for listing all the books in database#############################
list_book=Listbox(window, height=6,width=35)
list_book.grid(row=2,column=0,rowspan=6,columnspan=2)
list_book.bind('<<ListboxSelect>>',get_selected_row)#binding a method to the list box widget. bind will take 2 arguments the event and the function 

############################create the scrollbar#######################################
sb_list=Scrollbar(window)
sb_list.grid(row=2,column=2,rowspan=9)

############################now aplying configure method to listbox and grid#############################
list_book.configure(yscrollcommand=sb_list.set)# the vertical scrollbar along the y axis will set to this scrollbar
sb_list.configure(command=list_book.yview)#when u scroll the bar the vertical view of the list will change

#6 buttons namely viewall ,search entry, add entry, update, delete, close
b_view=Button(window,text="View All",width=12,command=view_command)
b_view.grid(row=2 ,column=3 )

b_search=Button(window,text="Search Entry",width=12,command=search_command)
b_search.grid(row=3 ,column=3 )

b_add=Button(window,text="Add Entry",width=12,command=add_command)
b_add.grid(row=4 ,column=3 )

b_update=Button(window,text="Update",width=12,command=update_command)
b_update.grid(row=5 ,column=3 )

b_del=Button(window,text="Delete",width=12,command=delete_command)
b_del.grid(row=6 ,column=3 )

b_close=Button(window,text="Close",width=12,command=window.destroy)
b_close.grid(row=7 ,column=3 )
window.mainloop() 

