import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import Paper from '@mui/material/Paper'

const App = () => {
  const [number, setNumber] = useState(0)
  const [version, setVersion] = useState('')
  const [allSessions, setAllSessions] = useState([])
  useEffect(() => {
    getInfo()
    getVersion()
  }, [])

  const getInfo = async () => {
    await axios.get('http://localhost:5555/get-info').then((res) => {
      setAllSessions(res.data.reverse())
    })
  }

  const getVersion = async () => {
    await axios.get('http://localhost:5555/get-version').then((res) => {
      setVersion(res.data.version)
    })
  }

  const onChangeHandle = (e) => {
    setNumber(e.target.value)
  }
  const onClickHandler = async () => {
    await axios.post('http://localhost:5555/log-session', {
      name: 'admin',
      number
    })
    await getInfo()
  }
  return (
    <div className='App'>
      <div style={{ margin: '10px 0' }}> {version} </div>
      <div>
        <TextField
          value={number}
          onChange={onChangeHandle}
          id='outlined-number'
          label='Number'
          type='number'
          InputLabelProps={{
            shrink: true
          }}
          style={{ marginTop: '10px' }}
        />
      </div>
      <div>
        <Button
          onClick={onClickHandler}
          style={{ marginTop: '20px' }}
          variant='contained'
        >
          Calculate
        </Button>
      </div>
      <div style={{ marginTop: '20px' }}>
        <TableContainer
          style={{ margin: 'auto' }}
          sx={{ width: 400 }}
          component={Paper}
        >
          <Table sx={{ width: 400 }} aria-label='simple table'>
            <TableHead>
              <TableRow>
                <TableCell>No</TableCell>
                <TableCell align='right'>Date </TableCell>
                <TableCell align='right'>Numbers</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {allSessions.map((row, index) => (
                <TableRow
                  key={index}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell align='right'>{index}</TableCell>
                  <TableCell align='right' scope='row'>
                    {row.datetime}
                  </TableCell>
                  <TableCell align='right'>{row.number}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>
  )
}

export default App
