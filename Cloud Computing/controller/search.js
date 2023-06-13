const sql = require("../config/database");
const util = require("util");

const Tookar = {
  // ADD DATA
  addByAll: (Customer_ID, kota, barang) => {
    return new Promise((resolve, reject) => {
      const query = `INSERT INTO mRecsys (Customer_ID, Kota, Barang) VALUES ('${Customer_ID}', '${kota}', '${barang}')`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
  // SEE ALL DATA
  seeAllData: () => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },

  // POST
  findByID: (Customer_ID) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Customer_ID = '${Customer_ID}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
  findByKota: (kota) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Kota = '${kota}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
  findByBarang: (barang) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Barang = '${barang}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },

  // GET
  getByID: (Customer_ID) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Customer_ID = '${Customer_ID}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
  getByKota: (kota) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Kota = '${kota}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
  getByBarang: (barang) => {
    return new Promise((resolve, reject) => {
      const query = `SELECT * FROM mRecsys WHERE Barang = '${barang}'`;
      sql.query(query, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  },
};
// ======================================= ADD DATA =======================================
const addAll = async (req, res) => {
  const params = req.query;
  const { Customer_ID, Kota, Barang } = params;

  try {
    await Tookar.addByAll(Customer_ID, Kota, Barang);

    res.status(200).send({
      error: false,
      message: "success",
      addedData: {
        Customer_ID: Customer_ID,
        Kota: Kota,
        Barang: Barang,
      },
    });
  } catch (err) {
    console.error("Error adding data to the database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// ======================================= SEE ALL DATA =======================================
const seeAll = async (req, res) => {
  try {
    const data = await Tookar.seeAllData();

    res.status(200).send({
      error: false,
      message: "success",
      data: data,
    });
  } catch (err) {
    console.error("Error retrieving data from the database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// ======================================= POST =======================================
// POST ID
const searchID = async (req, res) => {
  const params = req.body;
  const { Customer_ID } = params;

  try {
    const result = await Tookar.findByID(Customer_ID);

    if (result.length === 0) {
      res.status(405).send({ error: true, message: "Error on Post ID" });
    } else {
      const Tookar = {
        Customer_ID: result[0].Customer_ID,
        Kota: result[0].Kota,
        Barang: result[0].Barang,
      };

      res.status(200).send({
        error: false,
        message: "success",
        searchResult: {
          Customer_ID: Tookar.Customer_ID,
          Kota: Tookar.Kota,
          Barang: Tookar.Barang,
        },
      });
    }
  } catch (err) {
    console.error("Error retrieving user from database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// POST KOTA
const searchKota = async (req, res) => {
  const params = req.body;
  const { Customer_ID, kota, barang } = params;

  try {
    const result = await Tookar.findByKota(kota);

    if (result.length === 0) {
      res.status(405).send({ error: true, message: "Error on Post Kota" });
    } else {
      const Tookar = {
        Customer_ID: result[0].Customer_ID,
        Kota: result[0].Kota,
        Barang: result[0].Barang,
      };

      res.status(200).send({
        error: false,
        message: "success",
        searchResult: {
          Customer_ID: Tookar.Customer_ID,
          Kota: Tookar.Kota,
          Barang: Tookar.Barang,
        },
      });
    }
  } catch (err) {
    console.error("Error retrieving user from database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// POST BARANG
const searchBarang = async (req, res) => {
  const params = req.body;
  const { barang } = params;

  try {
    const result = await Tookar.findByBarang(barang);

    if (result.length === 0) {
      res.status(404).send({ error: true, message: "Error on Post Barang" });
    } else {
      const Tookar = {
        Customer_ID: result[0].Customer_ID,
        Kota: result[0].Kota,
        Barang: result[0].Barang,
      };

      res.status(200).send({
        error: false,
        message: "success",
        searchResult: {
          Customer_ID: Tookar.Customer_ID,
          Kota: Tookar.Kota,
          Barang: Tookar.Barang,
        },
      });
    }
  } catch (err) {
    console.error("Error retrieving user from database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// ======================================= GET =======================================
// GET ID
const getID = async (req, res) => {
  const params = req.query;
  const { Customer_ID } = params;

  try {
    const result = await Tookar.getByID(Customer_ID);

    if (result.length === 0) {
      res.status(405).send({ error: true, message: "Error on Get ID" });
    } else {
      const Tookar = {
        Customer_ID: result[0].Customer_ID,
        Kota: result[0].Kota,
        Barang: result[0].Barang,
      };

      res.status(200).send({
        error: false,
        message: "success",
        searchResult: {
          Customer_ID: Tookar.Customer_ID,
          Kota: Tookar.Kota,
          Barang: Tookar.Barang,
        },
      });
    }
  } catch (err) {
    console.error("Error retrieving user from database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// GET KOTA
const getKota = async (req, res) => {
  const params = req.params;
  const { kota } = params;

  try {
    const results = await Tookar.getByKota(kota);

    if (results.length === 0) {
      res.status(405).send({ error: true, message: "Error on Get Kota" });
    } else {
      const formattedResults = results.map((result) => ({
        Customer_ID: result.Customer_ID,
        Kota: result.Kota,
        Barang: result.Barang,
      }));

      res.status(200).send({
        error: false,
        message: "success",
        searchResults: formattedResults,
      });
    }
  } catch (err) {
    console.error("Error retrieving data from the database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};
// GET BARANG
const getBarang = async (req, res) => {
  const params = req.query;
  const { barang } = params;

  try {
    const result = await Tookar.getByBarang(barang);

    if (result.length === 0) {
      res.status(404).send({ error: true, message: "Error on Get Barang" });
    } else {
      const Tookar = {
        Customer_ID: result[0].Customer_ID,
        Kota: result[0].Kota,
        Barang: result[0].Barang,
      };

      res.status(200).send({
        error: false,
        message: "success",
        searchResult: {
          Customer_ID: Tookar.Customer_ID,
          Kota: Tookar.Kota,
          Barang: Tookar.Barang,
        },
      });
    }
  } catch (err) {
    console.error("Error retrieving user from database:", err);
    res.status(500).send({ error: true, message: "Internal Server Error" });
  }
};

module.exports = {
  addAll,
  searchBarang,
  searchKota,
  searchID,
  getBarang,
  getKota,
  getID,
  seeAll
};
