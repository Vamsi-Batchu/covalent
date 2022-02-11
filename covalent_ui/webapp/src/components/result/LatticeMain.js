/**
 * Copyright 2021 Agnostiq Inc.
 *
 * This file is part of Covalent.
 *
 * Licensed under the GNU Affero General Public License 3.0 (the "License").
 * A copy of the License may be obtained with this software package or at
 *
 *      https://www.gnu.org/licenses/agpl-3.0.en.html
 *
 * Use of this file is prohibited except in compliance with the License. Any
 * modifications or derivative works of this file must retain this copyright
 * notice, and modified files must contain a notice indicating that they have
 * been altered from the originals.
 *
 * Covalent is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
 *
 * Relief from the License may be granted by purchasing a commercial license.
 */

import { useEffect, useState } from 'react'
import ReactFlow, { Background, MiniMap } from 'react-flow-renderer'

import ElectronNode from '../graph/ElectronNode'
import ParameterNode from '../graph/ParameterNode'
import DirectedEdge from '../graph/DirectedEdge'
import layout from '../graph/Layout'
import LatticeControls from './LatticeControls'
import theme from '../../utils/theme'
import { lighten } from '@mui/material'
import { statusColor } from '../../utils/misc'
import useFitViewHelper from '../common/ReactFlowHooks'

const LatticeMain = ({
  graph,
  hasSelectedNode,
  marginLeft = 0,
  marginRight = 0,
}) => {
  const { fitView } = useFitViewHelper()

  const [elements, setElements] = useState()
  const [direction, setDirection] = useState('TB')
  const [showMinimap, setShowMinimap] = useState(false)
  const [showParams, setShowParams] = useState(false)
  const [nodesDraggable, setNodesDraggable] = useState(false)

  useEffect(() => {
    setElements(layout(graph, direction, showParams))
  }, [graph, direction, showParams])

  useEffect(() => {
    setTimeout(() => {
      fitView({ duration: 300, marginLeft, marginRight })
    })
  }, [
    fitView,
    hasSelectedNode,
    marginLeft,
    marginRight,
    graph,
    showParams,
    direction,
  ])

  // handle resizing
  useEffect(() => {
    const resizeHandler = () => {
      fitView({ duration: 300, marginLeft, marginRight })
    }
    window.addEventListener('resize', resizeHandler)
    return () => {
      window.removeEventListener('resize', resizeHandler)
    }
  })

  return (
    <>
      <ReactFlow
        nodeTypes={{ electron: ElectronNode, parameter: ParameterNode }}
        edgeTypes={{ directed: DirectedEdge }}
        nodesDraggable={nodesDraggable}
        nodesConnectable={false}
        elements={elements}
        // prevent selection when nothing is selected to prevent fitView
        selectNodesOnDrag={hasSelectedNode}
      >
        <Background
          variant="dots"
          color={lighten(theme.palette.background.paper, 0.05)}
          gap={12}
          size={1}
        />

        <LatticeControls
          marginLeft={marginLeft}
          marginRight={marginRight}
          showParams={showParams}
          toggleParams={() => {
            setShowParams(!showParams)
          }}
          showMinimap={showMinimap}
          toggleMinimap={() => {
            setShowMinimap(!showMinimap)
          }}
          direction={direction}
          setDirection={setDirection}
          nodesDraggable={nodesDraggable}
          toggleNodesDraggable={() => setNodesDraggable(!nodesDraggable)}
        />
        {showMinimap && (
          <MiniMap
            style={{ backgroundColor: theme.palette.background.default }}
            maskColor={theme.palette.background.paper}
            nodeColor={(node) => statusColor(node.data.status)}
          />
        )}
      </ReactFlow>
    </>
  )
}

export default LatticeMain
