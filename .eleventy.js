const MarkdownIt = require("markdown-it");

module.exports = function(eleventyConfig) {
  // Input/output directories
  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes"
    },
    pathPrefix: "/",
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};
