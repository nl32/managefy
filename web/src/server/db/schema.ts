// Example model schema from the Drizzle docs
// https://orm.drizzle.team/docs/sql-schema-declaration

import { SQL, relations, sql } from "drizzle-orm";
import { pgTable, integer, varchar, serial, date } from "drizzle-orm/pg-core";
/**
 * This is an example of how to use the multi-project schema feature of Drizzle ORM. Use the same
 * database instance for multiple projects.
 *
 * @see https://orm.drizzle.team/docs/goodies#multi-project-schema
 */

export const users = pgTable("user", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 256 }),
});

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(transactions),
}));

export const transactions = pgTable("transaction", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 256 }),
  date: date("date"),
  amount: integer("amount"),
  userId: integer("user_id"),
});

export const transactionRelations = relations(transactions, ({ one }) => ({
  user: one(users, { fields: [transactions.userId], references: [users.id] }),
}));
