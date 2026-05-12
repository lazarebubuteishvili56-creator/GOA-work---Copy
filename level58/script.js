//  Homework

// 1) for ციკლის საშუალებით 1 დან 20 ის ჩათვლით გამოიტანეთ მხოლოდ ლუწი რიცხვები

// 2) for ციკლის საშუალებით გადაუარეთ მასივს და შეამოწმეთ და გამოიტანეთ მხოლოდ ის რომლის სიგრძე იქნება 5

// for (let i = 1; i <= 20; i++) {
//   if (i % 2 === 0) {
//     console.log(i);
//   }
// }


let arr = ["lazo", "lika", "jemala", "nugzara", "pawo", "giviko"];

for (let i = 0; i < arr.length; i++) {
  if (arr[i].length === 5) {
    console.log(arr[i]);
  }
}
