#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
v_in10_NN_0vtk = LegacyVTKReader(FileNames=['C:\\Program Files\\blueCFD-Core-2017\\ofuser-of5\\run\\check\\V_in=1.0_NN\\VTK\\V_in=1.0_NN_0.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1002, 740]

# show data in view
v_in10_NN_0vtkDisplay = Show(v_in10_NN_0vtk, renderView1)
# trace defaults for the display properties.
v_in10_NN_0vtkDisplay.Representation = 'Surface'
v_in10_NN_0vtkDisplay.ColorArrayName = [None, '']
v_in10_NN_0vtkDisplay.OSPRayScaleArray = 'C'
v_in10_NN_0vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
v_in10_NN_0vtkDisplay.SelectOrientationVectors = 'C'
v_in10_NN_0vtkDisplay.ScaleFactor = 0.4
v_in10_NN_0vtkDisplay.SelectScaleArray = 'C'
v_in10_NN_0vtkDisplay.GlyphType = 'Arrow'
v_in10_NN_0vtkDisplay.GlyphTableIndexArray = 'C'
v_in10_NN_0vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
v_in10_NN_0vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
v_in10_NN_0vtkDisplay.ScalarOpacityUnitDistance = 0.36371927394484016
v_in10_NN_0vtkDisplay.GaussianRadius = 0.2
v_in10_NN_0vtkDisplay.SetScaleArray = ['POINTS', 'Cx']
v_in10_NN_0vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
v_in10_NN_0vtkDisplay.OpacityArray = ['POINTS', 'Cx']
v_in10_NN_0vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=v_in10_NN_0vtk)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.OSPRayScaleArray = 'C'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'C'
slice1Display.ScaleFactor = 0.4
slice1Display.SelectScaleArray = 'C'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'C'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.GaussianRadius = 0.2
slice1Display.SetScaleArray = ['POINTS', 'Cx']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Cx']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(v_in10_NN_0vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
slice1Display.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'Ux'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Ux'
uxLUT = GetColorTransferFunction('Ux')
uxLUT.RGBPoints = [-10.0, 0.231373, 0.298039, 0.752941, -0.5, 0.865003, 0.865003, 0.865003, 9.0, 0.705882, 0.0156863, 0.14902]
uxLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
uxLUT.RescaleTransferFunction(-10.6, 10.6)

# get opacity transfer function/opacity map for 'Ux'
uxPWF = GetOpacityTransferFunction('Ux')
uxPWF.Points = [-10.0, 0.0, 0.5, 0.0, 9.0, 1.0, 0.5, 0.0]
uxPWF.ScalarRangeInitialized = 1

# Rescale transfer function
uxPWF.RescaleTransferFunction(-10.6, 10.6)

# get color legend/bar for uxLUT in view renderView1
uxLUTColorBar = GetScalarBar(uxLUT, renderView1)
uxLUTColorBar.Title = 'Ux'
uxLUTColorBar.ComponentTitle = ''

# change scalar bar placement
uxLUTColorBar.Orientation = 'Horizontal'
uxLUTColorBar.WindowLocation = 'AnyLocation'
uxLUTColorBar.Position = [0.3421556886227546, 0.0445945945945946]
uxLUTColorBar.ScalarBarLength = 0.3299999999999996

# set active source
SetActiveSource(v_in10_NN_0vtk)

# show data in view
v_in10_NN_0vtkDisplay = Show(v_in10_NN_0vtk, renderView1)

# hide data in view
Hide(v_in10_NN_0vtk, renderView1)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0060213444053787216, 0.8649845884368418, 5.794619354882062]
renderView1.CameraFocalPoint = [-0.0060213444053787216, 0.8649845884368418, -0.252000704789296]
renderView1.CameraParallelScale = 2.29128784747792

# save screenshot
SaveScreenshot('C:/Program Files/blueCFD-Core-2017/ofuser-of5/run/check/V_in=1.0_NN/Ux.jpg', renderView1, ImageResolution=[1002, 740])

# set active source
SetActiveSource(slice1)

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'Uy'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uxLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Uy'
uyLUT = GetColorTransferFunction('Uy')
uyLUT.RGBPoints = [-0.9477149844169617, 0.231373, 0.298039, 0.752941, 0.0024490058422088623, 0.865003, 0.865003, 0.865003, 0.9526129961013794, 0.705882, 0.0156863, 0.14902]
uyLUT.ScalarRangeInitialized = 1.0

# Rescale transfer function
uyLUT.RescaleTransferFunction(-1.15, 1.15)

# get opacity transfer function/opacity map for 'Uy'
uyPWF = GetOpacityTransferFunction('Uy')
uyPWF.Points = [-0.9477149844169617, 0.0, 0.5, 0.0, 0.9526129961013794, 1.0, 0.5, 0.0]
uyPWF.ScalarRangeInitialized = 1

# Rescale transfer function
uyPWF.RescaleTransferFunction(-1.15, 1.15)

# get color legend/bar for uyLUT in view renderView1
uyLUTColorBar = GetScalarBar(uyLUT, renderView1)
uyLUTColorBar.Title = 'Uy'
uyLUTColorBar.ComponentTitle = ''

# change scalar bar placement
uyLUTColorBar.Orientation = 'Horizontal'
uyLUTColorBar.WindowLocation = 'AnyLocation'
uyLUTColorBar.Position = [0.34015968063872243, 0.0]
uyLUTColorBar.ScalarBarLength = 0.33000000000000024

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(v_in10_NN_0vtk)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0060213444053787216, 0.8649845884368418, 5.794619354882062]
renderView1.CameraFocalPoint = [-0.0060213444053787216, 0.8649845884368418, -0.252000704789296]
renderView1.CameraParallelScale = 2.29128784747792

# save screenshot
SaveScreenshot('C:/Program Files/blueCFD-Core-2017/ofuser-of5/run/check/V_in=1.0_NN/Uy.jpg', renderView1, ImageResolution=[1002, 740])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0060213444053787216, 0.8649845884368418, 5.794619354882062]
renderView1.CameraFocalPoint = [-0.0060213444053787216, 0.8649845884368418, -0.252000704789296]
renderView1.CameraParallelScale = 2.29128784747792

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).