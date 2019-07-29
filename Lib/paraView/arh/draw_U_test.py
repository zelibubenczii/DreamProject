#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
#tEST_R095_V30foam = GetActiveSource()

# destroy tEST_R095_V30foam
#Delete(tEST_R095_V30foam)
# tEST_R095_V30foam

# create a new 'Legacy VTK Reader'
tEST_R095_V30_0vtk = LegacyVTKReader(FileNames=['$DirPath$\\VTK\\$DirName$_0.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1002, 720]

# show data in view
tEST_R095_V30_0vtkDisplay = Show(tEST_R095_V30_0vtk, renderView1)
# trace defaults for the display properties.
tEST_R095_V30_0vtkDisplay.Representation = 'Surface'
tEST_R095_V30_0vtkDisplay.ColorArrayName = [None, '']
tEST_R095_V30_0vtkDisplay.OSPRayScaleArray = 'C'
tEST_R095_V30_0vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tEST_R095_V30_0vtkDisplay.SelectOrientationVectors = 'C'
tEST_R095_V30_0vtkDisplay.ScaleFactor = 0.4
tEST_R095_V30_0vtkDisplay.SelectScaleArray = 'C'
tEST_R095_V30_0vtkDisplay.GlyphType = 'Arrow'
tEST_R095_V30_0vtkDisplay.GlyphTableIndexArray = 'C'
tEST_R095_V30_0vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
tEST_R095_V30_0vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
tEST_R095_V30_0vtkDisplay.ScalarOpacityUnitDistance = 0.36371927394484016
tEST_R095_V30_0vtkDisplay.GaussianRadius = 0.2
tEST_R095_V30_0vtkDisplay.SetScaleArray = ['POINTS', 'Cx']
tEST_R095_V30_0vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
tEST_R095_V30_0vtkDisplay.OpacityArray = ['POINTS', 'Cx']
tEST_R095_V30_0vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set scalar coloring
ColorBy(tEST_R095_V30_0vtkDisplay, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
tEST_R095_V30_0vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tEST_R095_V30_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [1.0175277760037113e-21, 0.231373, 0.298039, 0.752941, 1.25, 0.865003, 0.865003, 0.865003, 2.5, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'

# change scalar bar placement
uLUTColorBar.Orientation = 'Horizontal'
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.33417165668662696, 0.0]
uLUTColorBar.ScalarBarLength = 0.32999999999999996

# reset view to fit data
renderView1.ResetCamera()

# Rescale transfer function
#uLUT.RescaleTransferFunction(1.01753e-21, 0.1)

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [1.0175277760037113e-21, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# Rescale transfer function
uPWF.RescaleTransferFunction(1.01753e-21, 0.1)

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 1.0, 7.316410272202349]
renderView1.CameraFocalPoint = [0.0, 1.0, 0.0]
renderView1.CameraParallelScale = 2.29128784747792

# save screenshot
SaveScreenshot('$DirPath$/images/U_test.jpg', renderView1, ImageResolution=[1002, 720])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 1.0, 7.316410272202349]
renderView1.CameraFocalPoint = [0.0, 1.0, 0.0]
renderView1.CameraParallelScale = 2.29128784747792

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).