# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt import QtCore
from qgis._gui import *
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/gui/qgsadvanceddigitizingdockwidget.h
QgsAdvancedDigitizingDockWidget.CadCapacities.baseClass = QgsAdvancedDigitizingDockWidget
CadCapacities = QgsAdvancedDigitizingDockWidget  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
QgsAdvancedDigitizingDockWidget.NoConstraint = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint.__doc__ = "No additional constraint"
QgsAdvancedDigitizingDockWidget.Perpendicular = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular.__doc__ = "Perpendicular"
QgsAdvancedDigitizingDockWidget.Parallel = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel.__doc__ = "Parallel"
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.__doc__ = 'Additional constraints which can be enabled\n\n' + '* ``NoConstraint``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint.__doc__ + '\n' + '* ``Perpendicular``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular.__doc__ + '\n' + '* ``Parallel``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel.__doc__
# --
# The following has been generated automatically from src/gui/qgsattributeeditorcontext.h
QgsAttributeEditorContext.Mode.baseClass = QgsAttributeEditorContext
# The following has been generated automatically from src/gui/attributetable/qgsattributetablefiltermodel.h
QgsAttributeTableFilterModel.FilterMode.baseClass = QgsAttributeTableFilterModel
QgsAttributeTableFilterModel.ColumnType.baseClass = QgsAttributeTableFilterModel
# The following has been generated automatically from src/gui/auth/qgsauthsettingswidget.h
QgsAuthSettingsWidget.WarningType.baseClass = QgsAuthSettingsWidget
# The following has been generated automatically from src/gui/qgscolorbutton.h
QgsColorButton.Behavior.baseClass = QgsColorButton
# The following has been generated automatically from src/gui/qgscolorwidgets.h
QgsColorTextWidget.ColorTextFormat.baseClass = QgsColorTextWidget
# The following has been generated automatically from src/gui/attributetable/qgsdualview.h
QgsDualView.ViewMode.baseClass = QgsDualView
QgsDualView.FeatureListBrowsingAction.baseClass = QgsDualView
# The following has been generated automatically from src/gui/qgsexpressionbuilderwidget.h
QgsExpressionBuilderWidget.Flag.baseClass = QgsExpressionBuilderWidget
Flag = QgsExpressionBuilderWidget  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgsfieldmappingmodel.h
# monkey patching scoped based enum
QgsFieldMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsFieldMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsFieldMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field QVariant::Type casted to (int)"
QgsFieldMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsFieldMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsFieldMappingModel.ColumnDataIndex.DestinationConstraints.__doc__ = "Destination field constraints"
QgsFieldMappingModel.ColumnDataIndex.__doc__ = 'The ColumnDataIndex enum represents the column index for the view\n\n' + '* ``SourceExpression``: ' + QgsFieldMappingModel.ColumnDataIndex.SourceExpression.__doc__ + '\n' + '* ``DestinationName``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationName.__doc__ + '\n' + '* ``DestinationType``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationType.__doc__ + '\n' + '* ``DestinationLength``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationLength.__doc__ + '\n' + '* ``DestinationPrecision``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ + '\n' + '* ``DestinationConstraints``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationConstraints.__doc__
# --
QgsFieldMappingModel.ColumnDataIndex.baseClass = QgsFieldMappingModel
# The following has been generated automatically from src/gui/qgsfilewidget.h
QgsFileWidget.StorageMode.baseClass = QgsFileWidget
QgsFileWidget.RelativeStorage.baseClass = QgsFileWidget
# The following has been generated automatically from src/gui/qgsfilterlineedit.h
QgsFilterLineEdit.ClearMode.baseClass = QgsFilterLineEdit
# The following has been generated automatically from src/gui/qgsfloatingwidget.h
QgsFloatingWidget.AnchorPoint.baseClass = QgsFloatingWidget
# The following has been generated automatically from src/gui/qgsfontbutton.h
QgsFontButton.Mode.baseClass = QgsFontButton
# The following has been generated automatically from src/gui/qgsgui.h
QgsGui.ProjectCrsBehavior.baseClass = QgsGui
# The following has been generated automatically from src/gui/qgsmapcanvasinteractionblocker.h
# monkey patching scoped based enum
QgsMapCanvasInteractionBlocker.Interaction.MapPanOnSingleClick.__doc__ = "A map pan interaction caused by a single click and release on the map canvas"
QgsMapCanvasInteractionBlocker.Interaction.__doc__ = 'Available interactions to block.\n\n' + '* ``MapPanOnSingleClick``: ' + QgsMapCanvasInteractionBlocker.Interaction.MapPanOnSingleClick.__doc__
# --
# The following has been generated automatically from src/gui/qgsmaplayeractionregistry.h
QgsMapLayerAction.Targets.baseClass = QgsMapLayerAction
Targets = QgsMapLayerAction  # dirty hack since SIP seems to introduce the flags in module
QgsMapLayerAction.Flags.baseClass = QgsMapLayerAction
Flags = QgsMapLayerAction  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgsmaptoolidentify.h
QgsMapToolIdentify.IdentifyMode.baseClass = QgsMapToolIdentify
QgsMapToolIdentify.LayerType.baseClass = QgsMapToolIdentify
LayerType = QgsMapToolIdentify  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/processing/qgsprocessingaggregatewidgets.h
# monkey patching scoped based enum
QgsAggregateMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsAggregateMappingModel.ColumnDataIndex.Aggregate.__doc__ = "Aggregate name"
QgsAggregateMappingModel.ColumnDataIndex.Delimiter.__doc__ = "Delimeter"
QgsAggregateMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsAggregateMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field QVariant::Type casted to (int)"
QgsAggregateMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsAggregateMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsAggregateMappingModel.ColumnDataIndex.__doc__ = 'The ColumnDataIndex enum represents the column index for the view\n\n' + '* ``SourceExpression``: ' + QgsAggregateMappingModel.ColumnDataIndex.SourceExpression.__doc__ + '\n' + '* ``Aggregate``: ' + QgsAggregateMappingModel.ColumnDataIndex.Aggregate.__doc__ + '\n' + '* ``Delimiter``: ' + QgsAggregateMappingModel.ColumnDataIndex.Delimiter.__doc__ + '\n' + '* ``DestinationName``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationName.__doc__ + '\n' + '* ``DestinationType``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationType.__doc__ + '\n' + '* ``DestinationLength``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationLength.__doc__ + '\n' + '* ``DestinationPrecision``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationPrecision.__doc__
# --
QgsAggregateMappingModel.ColumnDataIndex.baseClass = QgsAggregateMappingModel
# The following has been generated automatically from src/gui/processing/qgsprocessingtoolboxmodel.h
QgsProcessingToolboxProxyModel.Filters.baseClass = QgsProcessingToolboxProxyModel
Filters = QgsProcessingToolboxProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgssublayersdialog.h
QgsSublayersDialog.PromptMode.baseClass = QgsSublayersDialog
