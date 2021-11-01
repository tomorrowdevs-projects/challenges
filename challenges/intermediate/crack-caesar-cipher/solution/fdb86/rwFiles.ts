import {crackCaesar} from './hack-caesar'

const fs = require('fs')
const folder: string = '../../cases/'
const books = ['Shakespeare-Hamlet.txt', 'Shakespeare-Macbeth.txt', 'Shakespeare-Romeo-And-Juliet.txt']

function decryptFiles (path: string) {
  fs.readFile(path, 'utf8' , (err: string, data: string) => {
    if (err) {
      console.error(err)
      return
    }
    const decrypted_data: string = crackCaesar(data)

    fs.writeFile(path.slice(0, -4) + '-decrypted.txt', decrypted_data, (err: string) => {
      if (err) {
        console.error(err)
        return
      }
      console.log('file written successfully');
    })
  })
}


for (let i in books) {
  decryptFiles(folder+books[i])
}