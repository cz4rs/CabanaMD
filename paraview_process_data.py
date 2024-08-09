# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
dump_10pvtu = XMLPartitionedUnstructuredGridReader(
        registrationName='dump_10.pvtu*', FileName=[
    '/home/cz4rs/code/cabana/CabanaMD/dump_10.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_20.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_30.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_40.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_50.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_60.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_70.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_80.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_90.pvtu',
    '/home/cz4rs/code/cabana/CabanaMD/dump_100.pvtu'
])

# Properties modified on dump_10pvtu
dump_10pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

renderView1.ApplyIsometricView()
renderView1.AxesGrid.Visibility = 1


# get display properties
dump_10pvtuDisplay = GetDisplayProperties(dump_10pvtu, view=renderView1)

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=dump_10pvtu,
    GlyphType='Arrow')

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'Velocity'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')

# get 2D transfer function for 'Velocity'
velocityTF2D = GetTransferFunction2D('Velocity')

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-1.42767, 1.41958)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-1.42767, 1.41958)

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'Velocity']

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-1.42767, 1.41958)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-1.42767, 1.41958)

# Properties modified on glyph1
glyph1.ScaleFactor = 2.0
glyph1.GlyphMode = 'All Points'

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-1.42767, 1.41958)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-1.42767, 1.41958)

# create a new 'XML Partitioned Unstructured Grid Reader'
domain_act_10pvtu = XMLPartitionedUnstructuredGridReader(registrationName='domain_act_10.pvtu*', FileName=['/home/cz4rs/code/cabana/CabanaMD/domain_act_10.pvtu', '/home/cz4rs/code/cabana/CabanaMD/domain_act_20.pvtu'])

# Properties modified on domain_act_10pvtu
domain_act_10pvtu.TimeArray = 'None'

# show data in view
domain_act_10pvtuDisplay = Show(domain_act_10pvtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
domain_act_10pvtuDisplay.Representation = 'Surface'

# Rescale transfer function
velocityLUT.RescaleTransferFunction(-1.42767, 1.41958)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(-1.42767, 1.41958)

# change representation type
domain_act_10pvtuDisplay.SetRepresentationType('Wireframe')

# set scalar coloring
ColorBy(domain_act_10pvtuDisplay, ('CELLS', 'rank'))

# rescale color and/or opacity maps used to include current data range
domain_act_10pvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
domain_act_10pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rank'
rankLUT = GetColorTransferFunction('rank')

# get opacity transfer function/opacity map for 'rank'
rankPWF = GetOpacityTransferFunction('rank')

# get 2D transfer function for 'rank'
rankTF2D = GetTransferFunction2D('rank')

# Properties modified on domain_act_10pvtuDisplay
domain_act_10pvtuDisplay.LineWidth = 2.0

# reset view to fit data bounds
renderView1.ResetCamera(False, 0.9)

# update the view to ensure updated data information
renderView1.Update()

