// Use dynamic import() syntax for ES modules
import fetch from "node-fetch";

async function forkSpin(instances) {
  const spinPromises = Array.from({ length: instances }, (_, index) =>
    spin(index)
  );
  await Promise.all(spinPromises);
}

async function spin() {
  let i = 0;
  while (true) {
    const res = await fetch(
      "https://ma.oraimo.com/new-year/spin-to-win/luck.php?site=ma",
      {
        credentials: "include",
        headers: {
          "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
          Accept: "*/*",
          "Accept-Language": "en-GB,en;q=0.5",
          "X-Requested-With": "XMLHttpRequest",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-origin",
        },
        referrer: "https://ma.oraimo.com/new-year/spin-to-win/",
        method: "GET",
        mode: "cors",
      }
    );

    const json = await res.json();

    if (!JSON.stringify(json).includes("OFF Coupon")) {
      // Do something with the response that doesn't contain "OFF Coupon"
      fs.appendFileSync(
        "res.txt",
        "From spin : " + JSON.stringify(json) + "\n"
      );
      console.log("Main called", i++);
    } else {
      console.log("Skipped response with 'OFF Coupon'");
    }
  }
}

async function main() {
  const forkCount = 1500;

  console.log(`Forking ${forkCount} instances...`);

  await forkSpin(forkCount);

  console.log("All instances started.");
}

main().catch((err) => console.error("Main error:", err));
