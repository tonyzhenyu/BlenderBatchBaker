
from cgitb import text
from bpy.types import Panel

class BATCHBAKE_PT_PANEL(Panel): #N panel
    Panel.bl_space_type = "VIEW_3D"
    Panel.bl_region_type = "UI"

    Panel.bl_label = "BatchBake"
    Panel.bl_category = "Edit"# tabs in N panel

    def draw(self,context):
        layout = self.layout

        # properties
        myprops = context.scene.batchbake_properties#properties reference
        
        row_00 = layout.row(heading = 'Bake Multiple Objects')
        row_00.label(text="Bake Multiple Objects")
        layout.split(factor = 2 , align = True)

        row_01 =  layout.row(align= True)
        colmun_1 =row_01.column()
        column_2 = row_01.column()

        colmun_1.prop(myprops,property = "high_prefix",text = 'h') #Draw and Transfer properties value
        column_2.prop(myprops,property = "low_prefix",text = 'l') #Draw and Transfer properties value

        row_02 = layout.row()
        row_02.prop(myprops, "bake_collection")#Draw and Transfer properties value
        
        row_03 = layout.row()
        row_03.prop(myprops ,property = "cage_midlevel",text = 'Cage Size')

        row_03_1 = layout.row()
        row_03_1.prop(myprops,property = 'bake_type_enum',text='')# Enum type

        row_04 = layout.row()
        row_04.enabled = True
        row_04.operator("object.batch_bake_mods")# bind with ops bl_idname
         #end properties