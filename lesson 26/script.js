class fruit {
    constructor(name,color,taste,price){
        this.name = name;
        this.color = color;
        this.taste = taste;
        this.price = price;
    }
    
}
class fruitBasket {
    constructor(name,color,size,taste,price,vitamins,quantity){
        this.fruitBasketS(name,color,size,taste,price);
        this.vitamins = vitamins;
        this.quantity = quantity;
    }
        
}
 const a = new fruit("Apple","Red","Sweet",1.2)
 console.log(a.taste)

 const b = new fruitBasket("Banana","Yellow","medium","SSweet",0.5,"C, B6",10)
 console.log(b.vitamins)
