# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "BatchBake",
    "author" : "zhenyuhe",
    "description" : "Bake Multiple Object",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Bake"
}


import bpy

from . BatchBake_ops import BatchBakeOp, MyProperties
from . BatchBake_pnl import BATCHBAKE_PT_PANEL

classes = (MyProperties , BatchBakeOp , BATCHBAKE_PT_PANEL)

def register():
    for i in classes:
        bpy.utils.register_class(i)
        
    bpy.types.Scene.batchbake_properties = bpy.props.PointerProperty(type = MyProperties)#properties reference

def unregister():
    for i in classes:
        bpy.utils.unregister_class(i)
    
    del bpy.types.Scene.batchbake_properties
