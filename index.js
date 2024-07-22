const dropdown = document.getElementById("myDropdown");

dropdown.addEventListener("change", function() {
  const selectedOption = this.options[this.selectedIndex];
  if (selectedOption.value !== "") {
    window.location.href = selectedOption.value;
  }
});
