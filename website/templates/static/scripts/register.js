const formStep1 = document.querySelector(".form--step1");
let clientId;
const formStep2 = document.querySelector(".form--step2");
// const prevFormBtn = document.querySelector(".form__btn--prev");
const successMsg = document.querySelector(".success-message");
const selectRegion = document.querySelector(".select--region");

getRegions();

const clientName = document.querySelector(`[name="name"]`);
const phone = document.querySelector(`[name="phone"]`);
const nationalId = document.querySelector(`[name="nationalId"]`);
const password = document.querySelector(`[name="password"]`);

// Step1 validation
clientName.addEventListener("blur", () => {
  const isValidName = clientName.value.trim().split(" ").length >= 3;

  if (!isValidName) clientName.setAttribute("data-invalid", "true");
  else clientName.removeAttribute("data-invalid");
});

phone.addEventListener("keyup", () => limitBy(phone, 11));
phone.addEventListener("keydown", () => limitBy(phone, 11));

phone.addEventListener("blur", () => {
  const isValidNumber =
    phone.value.startsWith("01") && phone.value.length === 11;

  if (!isValidNumber) phone.setAttribute("data-invalid", "true");
  else phone.removeAttribute("data-invalid");
});

nationalId.addEventListener("keyup", () => limitBy(nationalId, 14));
nationalId.addEventListener("keydown", () => limitBy(nationalId, 14));

nationalId.addEventListener("blur", () => {
  const isValidId = nationalId.value.length === 14;

  if (!isValidId) nationalId.setAttribute("data-invalid", "true");
  else nationalId.removeAttribute("data-invalid");
});

password.addEventListener("blur", () => {
  const isValidPassword = password.value.length >= 8;

  if (!isValidPassword) password.setAttribute("data-invalid", "true");
  else password.removeAttribute("data-invalid");
});

formStep1.addEventListener("submit", async (e) => {
  e.preventDefault();

  const submitBtn = formStep1.querySelector(`[type="submit"]`);

  submitBtn.classList.add("btn--loading");
  submitBtn.textContent = "جار التحميل...";

  const isValidName = clientName.value.split(" ").length >= 3;
  const isValidNumber =
    phone.value.startsWith("01") && phone.value.length === 11;
  const isValidId = nationalId.value.length === 14;
  const isValidPassword = password.value.length >= 8;

  if (!isValidName) {
    clientName.setAttribute("data-invalid", "true");
    return;
  } else if (!isValidNumber) {
    phone.setAttribute("data-invalid", "true");
    return;
  } else if (!isValidId) {
    nationalId.setAttribute("data-invalid", "true");
    return;
  } else if (!isValidPassword) {
    password.setAttribute("data-invalid", "true");
    return;
  }

  const data = {
    name: clientName.value,
    phone: phone.value,
    nationalId: nationalId.value,
    password: password.value,
  };

  clientId = await postStepOne(data);

  formStep1.classList.add("hidden");
  formStep2.classList.remove("hidden");
});

// prevFormBtn.addEventListener("click", () => {
//   formStep1.classList.remove("hidden");
//   formStep2.classList.add("hidden");
// });

const area = document.querySelector(`[name="area"]`);
const streetName = document.querySelector(`[name="streetName"]`);
const buildingNumber = document.querySelector(`[name="buildingNumber"]`);
const apartementNumber = document.querySelector(`[name="apartmentNumber"]`);
const addressDetails = document.querySelector(`[name="addressDetails"]`);

// step2 validation
area.addEventListener("change", () => {
  const isValidArea = area.value !== "0";
  if (isValidArea) area.removeAttribute("data-invalid");
});

addressDetails.addEventListener("blur", () => {
  const isValidAddressDetails = addressDetails.value.length > 5;
  if (isValidAddressDetails) addressDetails.removeAttribute("data-invalid");
  else addressDetails.setAttribute("data-invalid", "true");
});

formStep2.addEventListener("submit", async (e) => {
  e.preventDefault();
  const submitBtn = formStep2.querySelector(`[type="submit"]`);

  submitBtn.classList.add("btn--loading");
  submitBtn.textContent = "جار التحميل...";

  const isValidArea = area.value !== "0";
  const isValidAddressDetails = addressDetails.value.length > 5;

  if (!isValidArea) {
    area.setAttribute("data-invalid", "true");
    return;
  } else if (!isValidAddressDetails) {
    addressDetails.setAttribute("data-invalid", "true");
    return;
  }

  const data = {
    clientId,
    area: document.querySelector(`[name="area"]`).value,
    streetName: document.querySelector(`[name="streetName"]`).value,
    buildingNumber: document.querySelector(`[name="buildingNumber"]`).value,
    apartementNumber: document.querySelector(`[name="apartmentNumber"]`).value,
    addressDetails: document.querySelector(`[name="addressDetails"]`).value,
  };

  const res = await postStepTwo(data);

  if (res.error !== undefined) {
    formStep2.classList.add("hidden");
    successMsg.classList.remove("hidden");
  }
});

async function getRegions() {
  const res = await fetch(
    "https://www.aswangreen.com/account/getAreas?format=json"
  );
  const data = await res.json();

  for (let i = 0; i < data.length; i++) {
    const option = document.createElement("option");
    option.value = data[i];
    option.textContent = data[i];

    selectRegion.appendChild(option);
  }
}

async function postStepOne(data) {
  try {
    const res = await fetch(
      "https://www.aswangreen.com/account/registerFirstStep",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    const clientData = await res.json();

    return clientData.clientId;
  } catch (error) {
    return { error };
  }
}

async function postStepTwo(data) {
  try {
    const res = await fetch(
      "https://www.aswangreen.com/account/registerFinal",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    res = await res.json();
    return res;
  } catch (error) {
    return { error };
  }
}

function limitBy(el, maxChar) {
  if (el.value.length > maxChar) {
    el.value = el.value.substring(0, maxChar);
  }
}
