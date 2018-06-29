# This is module to import. It provides VTKPythonAlgorithmBase, the base class
# for all python-based vtkAlgorithm subclasses in VTK and decorators used to
# 'register' the algorithm with ParaView along with information about UI.
from paraview.util.vtkAlgorithm import *

import numpy as np
import vtk

# Helpers:
from PVGeo import _helpers
# Classes to Decorate
from PVGeo.gslib import GSLibReader, SGeMSGridReader

@smproxy.reader(name="PVGeoGSLibReader",
       label="PVGeo: GSLib File Format",
       extensions="sgems dat geoeas gslib GSLIB txt SGEMS",
       file_description="GSLib Table")
class PVGeoGSLibReader(GSLibReader):
    def __init__(self):
        GSLibReader.__init__(self)

    #### Seters and Geters ####
    # @smproperty.stringvector(name="FileNames", panel_visibility="adcanced")
    # @smdomain.filelist()
    # @smhint.filechooser(extensions="sgems dat geoeas gslib GSLIB txt SGEMS", file_description="GSLib Tables")
    @smproperty.xml(_helpers.getFileReaderXml("sgems dat geoeas gslib GSLIB txt SGEMS", readerDescription='GSLib Table'))
    def AddFileName(self, fname):
        GSLibReader.AddFileName(self, fname)

    @smproperty.stringvector(name="Delimiter", default_values=" ")
    def SetDelimiter(self, deli):
        GSLibReader.SetDelimiter(self, deli)

    @smproperty.xml(_helpers.getPropertyXml('UseTab', 'Use Tab Delimiter', 'SetUseTab', False, help='A boolean to override the Delimiter_Field and use a Tab delimiter.'))
    def SetUseTab(self, flag):
        GSLibReader.SetUseTab(self, flag)

    @smproperty.intvector(name="SkipRows", default_values=0)
    def SetSkipRows(self, skip):
        GSLibReader.SetSkipRows(self, skip)

    @smproperty.stringvector(name="Comments", default_values="#")
    def SetComments(self, identifier):
        GSLibReader.SetComments(self, identifier)


##########


@smproxy.reader(name="PVGeoSGeMSGridReader",
       label="PVGeo: SGeMS Grid Reader",
       extensions="dat gslib sgems SGEMS",
       file_description="SGeMS Uniform Grid")
class PVGeoSGeMSGridReader(SGeMSGridReader):
    def __init__(self):
        SGeMSGridReader.__init__(self)


    #### Seters and Geters ####
    @smproperty.xml(_helpers.getFileReaderXml("sgems dat geoeas gslib GSLIB txt SGEMS", readerDescription='GSLib Table'))
    def AddFileName(self, fname):
        GSLibReader.AddFileName(self, fname)

    @smproperty.stringvector(name="Delimiter", default_values=" ")
    def SetDelimiter(self, deli):
        GSLibReader.SetDelimiter(self, deli)

    @smproperty.xml(_helpers.getPropertyXml('UseTab', 'Use Tab Delimiter', 'SetUseTab', False, help='A boolean to override the Delimiter_Field and use a Tab delimiter.'))
    def SetUseTab(self, flag):
        GSLibReader.SetUseTab(self, flag)

    @smproperty.intvector(name="SkipRows", default_values=0)
    def SetSkipRows(self, skip):
        GSLibReader.SetSkipRows(self, skip)

    @smproperty.stringvector(name="Comments", default_values="#")
    def SetComments(self, identifier):
        GSLibReader.SetComments(self, identifier)
