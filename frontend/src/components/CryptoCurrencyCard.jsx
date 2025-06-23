import { Card } from "antd";

function RoundToThree(number) {
  const roundedNumber = +number.toFixed(3);
  return roundedNumber;
}

function CryptoCurrencyCard(props) {

  const { currency } = props

  return (
      <div>
          <Card title={
              <div className="flex items-center gap-3">
                  <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
                  <span>{currency.name}</span>
              </div>
              }
          >
              <p>Текущая цена: {RoundToThree(currency.quote.USD.price)}$</p>
          </Card>
      </div>
  )
}

export default CryptoCurrencyCard
