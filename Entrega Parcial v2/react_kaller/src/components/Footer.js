import React from "react";

const Footer = () => {
  return (
    <div>
      <footer class="page-footer font-small blue ">
        <div class="footer-copyright text-center py-3  bg-dark text-white">
          &copy;{new Date().getFullYear()} Kaller Moraes
        </div>
      </footer>
    </div>
  );
};

export default Footer;
