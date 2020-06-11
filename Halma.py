file=open("output.txt","w")
from operator import attrgetter
import time,copy
start=time.time()
class AI:
	def __init__(self,Path,parent,Player,evaluation,children,From,To,Move,Board):
		self.Path = Path
		self.parent = parent
		self.Player = Player
		self.evaluation = evaluation
		self.children = children
		self.From = From 
		self.To = To
		self.Move = Move
		self.Board = Board

	def getAdjacentSpaces(x,y):
		spaces=[]
		spaces.append([x-1, y])
		spaces.append([x+1, y])  
		spaces.append([x, y-1])  
		spaces.append([x, y+1])
		spaces.append([x-1, y-1])
		spaces.append([x+1, y+1])  
		spaces.append([x+1, y-1])  
		spaces.append([x-1, y+1])
		return spaces

	def Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		z=copy.deepcopy(p)
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]=="." and (b,a) not in Target_Black and Jump_Flag==0:
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				q=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(q)
				Jump_Flag=0
				return 1
			elif Occupied[b][a]==1:
				Visited=copy.deepcopy(Occupied)
				if a==x and b==y-1 and y-2>=0 and Visited[y-2][x]==0:
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Visited[y+2][x]==0:
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Visited[y][x-2]==0:
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Visited[y][x+2]==0:
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Visited[y-2][x-2]==0:
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Visited[y+2][x+2]==0:
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Visited[y+2][x-2]==0:
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Visited[y-2][x+2]==0:
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI.Legal_Moves_in_to_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI.Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,[])
			if h==1:
				return 1
			else:
				p=z
		return 0

	def Legal_Moves_in(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		z=copy.deepcopy(p)
		condition=False
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]==0 and Jump_Flag==0:
				if Player=="WHITE":
					if a<=x and b<=y:
						condition=True
				else:
					if a>=x and b>=y:
						condition=True
				if condition==True:
					Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
					q=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
					Children.append(q)
					return 1
			elif Occupied[b][a]==1:
				Visited=copy.deepcopy(Occupied)
				if a==x and b==y-1 and y-2>=0 and Visited[y-2][x]==0:
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Visited[y+2][x]==0:
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Visited[y][x-2]==0:
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Visited[y][x+2]==0:
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Visited[y-2][x-2]==0:
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Visited[y+2][x+2]==0:
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Visited[y+2][x-2]==0:
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Visited[y-2][x+2]==0:
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
					if Player=="WHITE":
						if f<=c.current[0] and g<=c.current[1]:
							condition=True
					else:
						if f>=c.current[0] and g>=c.current[1]:
							condition=True
					if condition==True:
						Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
						Children.append(Child_Node)
						Reached.append([f,g])
						return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI.Legal_Moves_in(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Path)
					if h==1:
						return 1
					else:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI.Legal_Moves_in(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,[])
			if h==1:
				return 1
			else:
				p=z
		return

	def Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_White,In_Goal,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		z=copy.deepcopy(p)
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]==0 and (b,a) in Target_White and Jump_Flag==0 and In_Goal==True:
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				q=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(q)
				return 1
			elif Occupied[b][a]==0 and (b,a) not in Target_Black and In_Goal==False and Jump_Flag==0:
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				q=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(q)
				return 1
			elif Occupied[b][a]==1:
				Visited=copy.deepcopy(Occupied)
				if a==x and b==y-1 and y-2>=0 and Visited[y-2][x]==0:
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Visited[y+2][x]==0:
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Visited[y][x-2]==0:
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Visited[y][x+2]==0:
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Visited[y-2][x-2]==0:
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Visited[y+2][x+2]==0:
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Visited[y+2][x-2]==0:
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Visited[y-2][x+2]==0:
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(f,g),"J",Board)
							Children.append(Child_Node)
							Reached.append([f,g])
							return 1
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI.Legal_Moves_out(Neighbours1,f,g,Board,Target_Black,Visited,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==1:
						return 1
					else:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI.Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_White,In_Goal,Path)
			if h==1:
				return 1
			else:
				p=z
		return

class Move:
	def __init__(self,parent,current):
		self.parent = parent
		self.current = current

	def Reset_Board(Original,Changed):
		Changed=copy.deepcopy(Original)
		return Changed

class AI_Game:

	def Legal_Moves_in_to_out(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		z=copy.deepcopy(p)
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]==0 and (b,a) not in Target_Black and Jump_Flag==0:
				Board=copy.deepcopy(Board1)
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(Child_Node)
				Root_Node.children.append(Child_Node)
				Jump_Flag=0
			elif Occupied[b][a]==1:
				if a==x and b==y-1 and y-2>=0 and Occupied[y-2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Occupied[y+2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Occupied[y][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Occupied[y][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Occupied[y-2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Occupied[y+2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Occupied[y+2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Occupied[y-2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if c.current not in Target_Black and [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						Board=copy.deepcopy(Board1)
						Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
						Children.append(Child_Node)
						Root_Node.children.append(Child_Node)
						Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI_Game.Legal_Moves_in_to_out(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,[])
			if h==0:
				p=z
		return 0

	def Legal_Moves_in(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		condition=False
		z=copy.deepcopy(p)
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]==0 and Jump_Flag==0:
				if Player=="WHITE":
					if a<=x and b<=y:
						condition=True
				else:
					if a>=x and b>=y:
						condition=True
				if condition==True:
					Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
					Board=copy.deepcopy(Board1)
					Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
					Children.append(Child_Node)
					Root_Node.children.append(Child_Node)
					Jump_Flag=0
			elif Occupied[b][a]==1:
				if a==x and b==y-1 and y-2>=0 and Occupied[y-2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Occupied[y+2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Occupied[y][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Occupied[y][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Occupied[y-2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Occupied[y+2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Occupied[y+2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Occupied[y-2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if [f,g] not in Reached:
						while c.parent!=0:
							Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
							c=c.parent
						if Player=="WHITE":
							if f<=c.current[0] and g<=c.current[1]:
								condition=True
						else:
							if f>=c.current[0] and g>=c.current[1]:
								condition=True
						if condition==True:
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI_Game.Legal_Moves_in(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Path)
					if h==0:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI_Game.Legal_Moves_in(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,[])
			if h==0:
				p=z
		return 0

	def Legal_Moves_out(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,Target_White,In_Goal,Path):
		a=Neighbours[0][0]
		b=Neighbours[0][1]
		z=copy.deepcopy(p)
		if a>=0 and a<=15 and b>=0 and b<=15:
			if Occupied[b][a]==0 and (b,a) in Target_White and Jump_Flag==0 and In_Goal==True:
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				Board=copy.deepcopy(Board1)
				Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(Child_Node)
				Root_Node.children.append(Child_Node)
				Jump_Flag=0
			elif Occupied[b][a]==0 and (b,a) not in Target_Black and In_Goal==False and Jump_Flag==0:
				Path.append(["E",str(x)+',' +str(y),str(a)+','+str(b)])
				Board=copy.deepcopy(Board1)
				Child_Node=AI(Path,Root_Node,Player,0,[],(x,y),(a,b),"E",Board)
				Children.append(Child_Node)
				Root_Node.children.append(Child_Node)
				Jump_Flag=0
			elif Occupied[b][a]==1:
				if a==x and b==y-1 and y-2>=0 and Occupied[y-2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x]=1
					q=Move(p,(x,y-2))
					p=Move(q.parent,(x,y-2))
					c=copy.deepcopy(q)
					f=x
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y-2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x and b==y+1 and y+2<=15 and Occupied[y+2][x]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x]=1
					q=Move(p,(x,y+2))
					p=Move(q.parent,(x,y+2))
					c=copy.deepcopy(q)
					f=x
					g=y+2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x,y+2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y and x-2>=0 and Occupied[y][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x-2]=1
					q=Move(p,(x-2,y))
					p=Move(q.parent,(x-2,y))
					c=copy.deepcopy(q)
					f=x-2
					g=y
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y and x+2<=15 and Occupied[y][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y][x+2]=1
					q=Move(p,(x+2,y))
					p=Move(q.parent,(x+2,y))
					c=copy.deepcopy(q)
					f=x+2
					g=y
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y-1 and x-2>=0 and y-2>=0 and Occupied[y-2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x-2]=1
					q=Move(p,(x-2,y-2))
					p=Move(q.parent,(x-2,y-2))
					c=copy.deepcopy(q)
					f=x-2
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y-2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y+1 and x+2<=15 and y+2<=15 and Occupied[y+2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x+2]=1
					q=Move(p,(x+2,y+2))
					p=Move(q.parent,(x+2,y+2))
					c=copy.deepcopy(q)
					f=x+2
					g=y+2					
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y+2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x-1 and b==y+1 and x-2>=0 and y+2<=15 and Occupied[y+2][x-2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y+2][x-2]=1
					q=Move(p,(x-2,y+2))
					p=Move(q.parent,(x-2,y+2))
					c=copy.deepcopy(q)
					f=x-2
					g=y+2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x-2,y+2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
				elif a==x+1 and b==y-1 and x+2<=15 and y-2>=0 and Occupied[y-2][x+2]==0:
					Visited=copy.deepcopy(Occupied)
					Visited[y-2][x+2]=1
					q=Move(p,(x+2,y-2))
					p=Move(q.parent,(x+2,y-2))
					c=copy.deepcopy(q)
					f=x+2
					g=y-2
					if In_Goal==True:
						if c.current in Target_White and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					else:
						if c.current not in Target_Black and [f,g] not in Reached:
							while c.parent!=0:
								Path.append(["J",str(c.parent.current[0])+","+str(c.parent.current[1]),str(c.current[0])+","+str(c.current[1])])
								c=c.parent
							Board=copy.deepcopy(Board1)
							Child_Node=AI(Path,Root_Node,Player,0,[],(c.current[0],c.current[1]),(f,g),"J",Board)
							Children.append(Child_Node)
							Root_Node.children.append(Child_Node)
							Reached.append([f,g])
					Neighbours1=AI.getAdjacentSpaces(x+2,y-2)
					h=AI_Game.Legal_Moves_out(Neighbours1,f,g,Board1,Target_Black,Visited,Root_Node,Children,Player,1,p,q,Reached,Target_White,In_Goal,Path)
					if h==0:
						p=z
		del Neighbours[0]
		while Neighbours!=[]:
			h=AI_Game.Legal_Moves_out(Neighbours,x,y,Board1,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,Reached,Target_White,In_Goal,[])
			if h==0:
				p=z
		return 0

	def Games(Player,Board,Root_Node):
		Position_White=[]
		Position_Black=[]
		Target_White=[(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(0,4),(1,4)]
		Target_Black=[(14,11),(15,11),(13,12),(14,12),(15,12),(12,13),(13,13),(14,13),(15,13),(11,14),(12,14),(13,14),(14,14),(15,14),(11,15),(12,15),(13,15),(14,15),(15,15)]
		count=0
		Occupied=[[0 for i in range(0,16)] for j in range(0,16)]
		Children=[]
		Jump_Flag=0
		for i in range(0,16):
			for j in range(0,16):
				if Board[j][i]=='W':
					Position_White.append((j,i))
					Occupied[j][i]=1
				elif Board[j][i]=='B':
					Position_Black.append((j,i))
					Occupied[j][i]=1
		Board_Original_Copy=copy.deepcopy(Board)
		if Player=="WHITE":
			for i in range(0,19):
				y=Position_White[i][0]
				x=Position_White[i][1]
				if (y,x) in Target_Black:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],[])
					Jump_Flag=0
			if Children==[]:
				for i in range(0,19):
					y=Position_White[i][0]
					x=Position_White[i][1]
					if (y,x) in Target_Black:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_in(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],[])
						Jump_Flag=0
			if Children==[]:
				for i in range(0,19):
					y=Position_White[i][0]
					x=Position_White[i][1]
					p=Move(0,(x,y))
					if (y,x) in Target_White:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],Target_White,True,[])
						Jump_Flag=0
					elif (y,x) not in Target_White and (y,x) not in Target_Black:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],Target_White,False,[])
						Jump_Flag=0
		elif Player=="BLACK":
			for i in range(0,19):
				y=Position_Black[i][0]
				x=Position_Black[i][1]
				if (y,x) in Target_White:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					h=AI_Game.Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],[])
					Jump_Flag=0
			if Children==[]:
				for i in range(0,19):
					y=Position_Black[i][0]
					x=Position_Black[i][1]
					if (y,x) in Target_White:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_in(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],[])
						Jump_Flag=0
			if Children==[]:
				for i in range(0,19):
					y=Position_Black[i][0]
					x=Position_Black[i][1]
					p=Move(0,(x,y))
					if (y,x) in Target_Black:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],Target_Black,True,[])
						Jump_Flag=0
					elif (y,x) not in Target_White and (y,x) not in Target_Black:
						Neighbours=AI.getAdjacentSpaces(x,y)
						p=Move(0,(x,y))
						q=Move(p,0)
						h=AI_Game.Legal_Moves_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children,Player,Jump_Flag,p,q,[],Target_Black,False,[])
						Jump_Flag=0
		return Children

	def sqrt_dist(x,y):
		return pow(pow(x[0]-y[0],2)+pow(x[1]-y[1],2),0.5)

	def Evaluation(Node,Board):		
		dist=0
		if Node.Player=="WHITE":
			for i in range(0,16):
				for j in range(0,16):
					if Board[j][i]=="W":
						dist+=pow(pow(j,2)+pow(i,2),0.5)
		else:
			for i in range(0,16):
				for j in range(0,16):
					if Board[j][i]=="B":
						dist+=pow(pow(j-15,2)+pow(i-15,2),0.5)
		Node.evaluation=dist*-1
		return dist*-1

	def Evaluation_1(Node,Board):	
		value=0
		if Node.Player=="WHITE":
			Target_White=[(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(0,4),(1,4)]
			for i in range(0,16):
				for j in range(0,16):
					if Board[j][i]=="W":
						distances = [AI_Game.sqrt_dist((j,i), goal) for goal in Target_White if Board[goal[0]][goal[1]] != "W"]
						if len(distances):
							value += max(distances)
						else:
							value += -50	
		else:
			Target_Black=[(14,11),(15,11),(13,12),(14,12),(15,12),(12,13),(13,13),(14,13),(15,13),(11,14),(12,14),(13,14),(14,14),(15,14),(11,15),(12,15),(13,15),(14,15),(15,15)]
			for i in range(0,16):
				for j in range(0,16):
					if Board[j][i]=="B":
						distances = [AI_Game.sqrt_dist((j,i), goal) for goal in Target_Black if Board[goal[0]][goal[1]] != "B"]
						if len(distances):
							value += max(distances)
						else:
							value += -50
		Node.evaluation=value*-1
		return value*-1

	def Min_Max(Root_Node,depth,isMaximizingPlayer,Alpha,Beta,Player,cutoff):
		if depth==cutoff:
			if Root_Node.Player=="WHITE":
				Root_Node.Player="BLACK"
			else:
				Root_Node.Player="WHITE"
			return AI_Game.Evaluation(Root_Node,Root_Node.Board),Root_Node
		if isMaximizingPlayer:
			Best_Val = -999999
			children = AI_Game.Games(Root_Node.Player,Root_Node.Board,Root_Node)
			if children==[]:
				return 0,Root_Node
			n=len(children)
			for i in range(0,n):
				if Root_Node.Player=="WHITE":
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="W"
				else:
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="B"
			for j in children:
				if j.Player=="WHITE":
					j.Player="BLACK"
				else:
					j.Player="WHITE"
			for x in range(0,n):
				Node=children[x]
				value,Move = AI_Game.Min_Max(Node,depth+1,False,Alpha,Beta,Node.Player,cutoff)
				if Best_Val<=value:
					Best_Val=value
				if Best_Val==value:
					Best_Move=Node
				Alpha = max(Alpha,Best_Val)
				if Beta<=Alpha:
					break
			return Best_Val,Best_Move
		else:
			Best_Val = 999999
			children = AI_Game.Games(Root_Node.Player,Root_Node.Board,Root_Node)
			if children==[]:
				return 0,Root_Node
			n=len(children)
			for i in range(0,n):
				if Root_Node.Player=="WHITE":
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="W"
				else:
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="B"
			for j in children:
				if j.Player=="WHITE":
					j.Player="BLACK"
				else:
					j.Player="WHITE"
			for x in range(0,n):
				Node=children[x]
				value,Move = AI_Game.Min_Max(Node,depth+1,True,Alpha,Beta,Node.Player,cutoff)
				Best_Val = min(Best_Val,value)
				if Best_Val==value:
					Best_Move=Node
				Beta = min(Beta,Best_Val)
				if Beta<=Alpha:
					break
			return Best_Val,Best_Move

	def Min_Max_1(Root_Node,depth,isMaximizingPlayer,Alpha,Beta,Player,cutoff):
		if Player=="WHITE":
			goal=[(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(0,4),(1,4)]
		else:
			goal=[(14,11),(15,11),(13,12),(14,12),(15,12),(12,13),(13,13),(14,13),(15,13),(11,14),(12,14),(13,14),(14,14),(15,14),(11,15),(12,15),(13,15),(14,15),(15,15)]
		if depth==cutoff:
			if Root_Node.parent.From not in goal and Root_Node.parent.To in goal and Root_Node.To in goal:
				return AI_Game.Evaluation_1(Root_Node,Root_Node.Board),Root_Node
			else:
				return AI_Game.Evaluation(Root_Node,Root_Node.Board),Root_Node
		if isMaximizingPlayer:
			Best_Val = -999999
			children = AI_Game.Games(Root_Node.Player,Root_Node.Board,Root_Node)
			if children==[]:
				return 0,Root_Node
			n=len(children)
			for i in range(0,n):
				if Root_Node.Player=="WHITE":
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="W"
				else:
					children[i].Board[children[i].From[1]][children[i].From[0]]="."
					children[i].Board[children[i].To[1]][children[i].To[0]]="B"
			for x in range(0,n):
				Node=children[x]
				value,Move = AI_Game.Min_Max_1(Node,depth+1,True,Alpha,Beta,Node.Player,cutoff)
				if Best_Val<=value:
					Best_Val=value
				if Best_Val==value:
					Best_Move=Node
				Alpha = max(Alpha,Best_Val)
				if Beta<=Alpha:
					break
			return Best_Val,Best_Move

class Halma:

	def Single(Player,Target_White,Target_Black,Board):
		Position_White=[]
		Position_Black=[]
		count=0
		Occupied=[[0 for i in range(0,16)] for j in range(0,16)]
		Children=[]
		Children_Node_Array=[]
		Jump_Flag=0
		Path=[]
		for i in range(0,16):
			for j in range(0,16):
				if Board[j][i]=='W':
					Position_White.append((j,i))
					Occupied[j][i]=1
				elif Board[j][i]=='B':
					Position_Black.append((j,i))
					Occupied[j][i]=1
		Root_Node = AI(Path,0,Player,0,[],0,0,"",Board)
		Board_Original_Copy=copy.deepcopy(Board)
		if Player=="WHITE":
			for i in range(0,19):
				y=Position_White[i][0]
				x=Position_White[i][1]
				if (y,x) in Target_Black:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
			for i in range(0,19):
				y=Position_White[i][0]
				x=Position_White[i][1]
				if (y,x) in Target_Black:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_in(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
			for i in range(0,19):
				y=Position_White[i][0]
				x=Position_White[i][1]
				p=Move(0,(x,y))
				if (y,x) in Target_White:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_White,True,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
				elif (y,x) not in Target_White and (y,x) not in Target_Black:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_out(Neighbours,x,y,Board,Target_Black,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_White,False,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
		elif Player=="BLACK":
			for i in range(0,19):
				y=Position_Black[i][0]
				x=Position_Black[i][1]
				if (y,x) in Target_White:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_in_to_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
			for i in range(0,19):
				y=Position_Black[i][0]
				x=Position_Black[i][1]
				if (y,x) in Target_White:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_in(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
			for i in range(0,19):
				y=Position_Black[i][0]
				x=Position_Black[i][1]
				p=Move(0,(x,y))
				if (y,x) in Target_Black:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_Black,True,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0
				elif (y,x) not in Target_Black and (y,x) not in Target_White:
					Neighbours=AI.getAdjacentSpaces(x,y)
					p=Move(0,(x,y))
					q=Move(p,0)
					Reached=[]
					h=AI.Legal_Moves_out(Neighbours,x,y,Board,Target_White,Occupied,Root_Node,Children_Node_Array,Children,Player,Board_Original_Copy,Jump_Flag,p,q,Reached,Target_Black,False,Path)
					if h==1:
						path=Children[0].Path[::-1]
						n=len(path)
						for m in range(0,n-1):
							file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
						file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
						return
					Jump_Flag=0

	if __name__=="__main__":
		file1=open("input.txt","r")
		a=file1.readlines()
		file1.close()
		a=[x.rstrip('\n') for x in a]
		Game=a[0]
		Player=a[1]
		Time=a[2]
		Target=[]
		Board=[]
		Board1=[[0 for i in range(0,16)] for j in range(0,16)]
		Target_White=[(0,0),(1,0),(2,0),(3,0),(4,0),(0,1),(1,1),(2,1),(3,1),(4,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(0,4),(1,4)]
		Target_Black=[(14,11),(15,11),(13,12),(14,12),(15,12),(12,13),(13,13),(14,13),(15,13),(11,14),(12,14),(13,14),(14,14),(15,14),(11,15),(12,15),(13,15),(14,15),(15,15)]
		for i in range(0,16):
			Board.append(a[3+i])
		for i in range(0,16):
			for j in range(0,16):
				Board1[i][j]=Board[i][j]
		if Game=="SINGLE":
			Single(Player,Target_White,Target_Black,Board1)
		elif Game=="GAME":
			count=0
			Node = AI([],0,Player,0,[],0,0,"",Board1)
			cutoff=2
			if Player=="BLACK":
				for i in range(10,16):
					for j in range(10,16):
						if Board1[j][i]=="B":
							count+=1
			else:
				for i in range(0,6):
					for j in range(0,6):
						if Board1[j][i]=="W":
							count+=1
			if count<17:
				cutoff=1
			if cutoff==1:
				Best,Nodes=AI_Game.Min_Max(Node,0,True,-999999,999999,Player,cutoff)
			else:
				Best,Nodes=AI_Game.Min_Max_1(Node,0,True,-999999,999999,Player,cutoff)
			n=len(Nodes.Path)
			if n>1:
				path=Nodes.Path[::-1]
				for m in range(0,n-1):
					file.write(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
					print(path[m][0]+" "+path[m][1]+" "+path[m][2]+"\n")
				file.write(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
				print(path[n-1][0]+" "+path[n-1][1]+" "+path[n-1][2])
			else:
				file.write(Nodes.Path[0][0]+" "+Nodes.Path[0][1]+" "+Nodes.Path[0][2])
				print(Nodes.Path[0][0]+" "+Nodes.Path[0][1]+" "+Nodes.Path[0][2])
print(time.time()-start)