"use strict";
const guests_inviteTab = document.querySelector("#list-users");
const guests_removeTab = document.querySelector("#list-guests");

let selectedGuest = undefined;
let selectedUser = undefined;

// class App {
//   constructor() {
//     console.log("Constructor");
//   }
//   // _captureRowGuests(e) {
//   //   console.log("I am reading it!");
//   //   const listitem = e.target.closest(".list-group-item");
//   //   if (!listitem) return;
//   //   console.log("I am reading it!");
//   // }
// }

// const app = new App();

function guests_userElementSelected(el) {
  if (selectedUser) {
    selectedUser.classList.remove("active");
    const btn = document.querySelector("#btn-add");
    btn.remove();
  }
  selectedUser = el;
  selectedUser.classList.add("active");
  if (selectedGuest) selectedGuest.classList.remove("active");

  console.log("A user in the users list was selected");
  guests_inviteTab.classList.add("show");
  guests_inviteTab.classList.add("active");

  guests_removeTab.classList.remove("show");
  guests_removeTab.classList.remove("active");

  const html = `<a href="/lists/guests/add/${el.dataset.listslug}/${el.id
    .split("-")
    .at(
      -1
    )}" class="btn btn-outline-secondary btn_list_item_bottom" id="btn-add">Add</a>`;
  guests_inviteTab.insertAdjacentHTML("afterbegin", html);
  console.log(guests_inviteTab);
}

function guests_guestlementSelected(el) {
  if (selectedGuest) {
    selectedGuest.classList.remove("active");
    const btn = document.querySelector("#btn-remove");
    btn.remove();
  }

  selectedGuest = el;
  selectedGuest.classList.add("active");
  if (selectedUser) selectedUser.classList.remove("active");
  console.log("A user in the guest list was selected");
  guests_removeTab.classList.add("show");
  guests_removeTab.classList.add("active");

  guests_inviteTab.classList.remove("show");
  guests_inviteTab.classList.remove("active");

  const html = `<a href="/lists/guests/remove/${el.dataset.listslug}/${el.id
    .split("-")
    .at(
      -1
    )}" class="btn btn-outline-secondary btn_list_item_bottom" id="btn-remove">Remove</a>`;
  guests_removeTab.insertAdjacentHTML("afterbegin", html);
  console.log(guests_removeTab);
}
