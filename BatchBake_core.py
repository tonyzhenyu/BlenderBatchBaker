import bpy

#--properties--
# high_prefix = 'h.'
# low_prefix = 'l.'
# direct_collection_name = 'bake'
#--properties--

class MyBaker:
    high_obj = []
    low_obj = []
    cages_obj = []

    h_prefix = 'h.' 
    l_prefix = 'l.'
    collection_b = 'bake'

    bake_type = 'NORMAL'
    cage_prefix = 'cage.'
    cage_midlevel = 0.95
    #Initialize
    def __init__(self,h,l,collection):
        self.h_prefix = h
        self.l_prefix = l
        self.collection_b = collection
        pass
    #Initialize

    def SelectCollection(self):
        bpy.ops.object.select_same_collection(collection = self.collection_b)

        for i in bpy.context.selected_objects:
            if i.name.startswith(self.h_prefix):
                self.high_obj.append(i)
            elif i.name.startswith(self.l_prefix):
                self.low_obj.append(i)

    #Set Object RenderState
    def SetRenderState(self,state = True , index = 0):
        self.high_obj[index].hide_render = state
        self.low_obj[index].hide_render = state

        #return 0

    def Bake(self,index = 0):
        
        bpy.ops.object.select_all(action = 'DESELECT')

        self.SetRenderState(False,index)
        
        self.high_obj[index].select_set(True)
        self.low_obj[index].select_set(True)

        bpy.context.view_layer.objects.active = self.low_obj[index] # active object

        bpy.context.scene.render.bake.cage_object = self.cages_obj[index]
        bpy.context.scene.render.bake.use_cage = True
        
        bpy.ops.object.bake(type = self.bake_type,use_selected_to_active = True, use_clear = False , use_cage = True, 
        cage_object = self.cages_obj[index].name
        )

        pass

    def CageProxy(self,index = 0): #Generate Cage

        bpy.ops.object.select_all(action = 'DESELECT')
        bpy.context.view_layer.objects.active = self.low_obj[index]                     # SetLowMesh active
        self.low_obj[index].select_set(True)
        bpy.ops.object.duplicate(False)                                                 # Duplicate Obj

        bpy.context.view_layer.objects.active.name = self.low_obj[index].name.replace(self.l_prefix , self.cage_prefix)
        bpy.ops.object.modifier_add(type = 'DISPLACE')                                  # Add Modifier
        bpy.context.view_layer.objects.active.modifiers['Displace'].mid_level = self.cage_midlevel    # set midlevel
        bpy.context.view_layer.objects.active.display_type = 'WIRE'                     # Set display mode wire
        bpy.context.view_layer.objects.active.hide_render = False

        self.cages_obj.append(bpy.context.view_layer.objects.active)                    # Add Duplicate Obj To List
        pass

    #Bake(index = 2)
    #SetRenderState(state = False)

    def Execute(self):
        bpy.context.scene.render.engine = 'CYCLES'
        self.SelectCollection()

        for i in range(0,len(self.low_obj)):
            self.SetRenderState(True,i)

        for i in range(0 , len(self.low_obj)):
            self.CageProxy(i)
            self.Bake(i)
            self.SetRenderState(False,i)

        bpy.ops.object.select_all(action = 'DESELECT')
        for i in self.cages_obj:
            i.select_set(True)
            bpy.ops.object.delete(use_global = False)

        self.cages_obj.clear()
        self.low_obj.clear()
        self.high_obj.clear()
        pass

