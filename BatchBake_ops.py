
import bpy

from bpy.types import Operator ,PropertyGroup
from bpy.props import StringProperty
from bpy.props import FloatProperty
from bpy.props import EnumProperty
from . BatchBake_core import MyBaker

class MyProperties(PropertyGroup):
    high_prefix : StringProperty(name = "h.prefix",default = "h.")
    low_prefix : StringProperty(name = "l.prefix",default = "l.")
    bake_collection : StringProperty(name = "collection",default = "bake")
    cage_midlevel : FloatProperty(name = "cage midlevel" ,default = 0.95 , soft_min=0,soft_max=1)
    bake_type_enum : EnumProperty(name = 'Bake Type',description ='Bake Type', 
    items=[('NORMAL','Normal','',0),
    ('EMIT','Emit','',1),
    ('AO','Ambient Occlusion','',2),
    ('SHADOW','Shadow','',3),
    ('POSITION','Position','',4),
    ('ROUGHNESS','Roughness','',5)
    ])

class BatchBakeOp(Operator):
    bl_idname = "object.batch_bake_mods" #use to bind 
    bl_label = "Bake"
    bl_description = "Bake All Object from collection "

    @classmethod #static method
    def poll(cls , context):
        return context.object is not None
        
    def execute(self , context):

        #bind props
        myprops = context.scene.batchbake_properties

        print(myprops.high_prefix)
        print(myprops.low_prefix)
        print(myprops.bake_collection)
        print(myprops.bake_type_enum)

        baker = MyBaker(myprops.high_prefix, myprops.low_prefix , myprops.bake_collection)
        baker.cage_midlevel = myprops.cage_midlevel

        baker.bake_type = myprops.bake_type_enum
        baker.Execute()
        return {'FINISHED'}